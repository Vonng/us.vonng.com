HUGO ?= hugo
OINK_LOCAL ?= $(HOME)/pgsty/oink
PORT ?= 1318

# Production uses themes/oink; dev uses the selected local checkout.
export GOWORK := off
export HUGO_MODULE_WORKSPACE := off
PINNED_HUGO = env -u HUGO_MODULE_REPLACEMENTS $(HUGO)
LOCAL_HUGO = env -u HUGO_MODULE_REPLACEMENTS $(HUGO) --themesDir "$(abspath $(OINK_LOCAL)/..)" --theme "$(notdir $(abspath $(OINK_LOCAL)))"

.PHONY: build check preview sync check-drafts browser
DESTINATION ?= public
build:
	$(PINNED_HUGO) --destination "$(DESTINATION)" --cleanDestinationDir --gc --minify --environment production --printPathWarnings --panicOnWarning
check: build
	python3 scripts/check_site.py --public-dir "$(DESTINATION)"
check-drafts:
	python3 scripts/check_draft_behavior.py
sync:
	python3 scripts/sync_public.py --source .cache/production-review
preview:
	python3 scripts/serve_preview.py
browser:
	node scripts/check_browser.mjs

dev: theme-local
	$(LOCAL_HUGO) server --renderToMemory --bind 127.0.0.1 --port "$(PORT)" --noBuildLock

.PHONY: dev

# Fail explicitly if a local theme was requested but is unavailable.
theme-local:
	@test -f "$(OINK_LOCAL)/hugo.yaml" || { echo "Set OINK_LOCAL to an OINK checkout (default: ~/pgsty/oink)." >&2; exit 1; }

.PHONY: theme-local
