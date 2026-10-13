.PHONY: build check preview sync check-drafts browser
DESTINATION ?= public
build:
	hugo --destination "$(DESTINATION)" --cleanDestinationDir --gc --minify --environment production --printPathWarnings --panicOnWarning
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
