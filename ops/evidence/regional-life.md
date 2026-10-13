# 区域生活比较：作者事实链

实际查阅：2026-10-13。作者 `/root/health`，B05。对应 `content/book/foundations/geography/regional-life.md`。本文件是作者记录，不代替异人事实审。除特别注明外，均通过 `web.open` 实际读取正文，搜索摘要仅用于发现入口。

## 采用来源与定位

| 正文断言 / 来源 | 实际原文位置、时期与边界 |
|---|---|
| [Census Geographic Levels](https://www.census.gov/programs-surveys/economic-census/guidance-geographies/levels.html)：四区域、九 division、所选州与 DC 分组 | `Regions and Divisions`，正文行 276—293，完整列明各分组。该页其他节含 2012 Economic Census 旧定义，**仅采用稳定区域清单**，未采用其旧版 metro / urban cluster 术语。另实读 [Survey Explorer Geographies](https://www.census.gov/data/data-tools/survey-explorer/geo.html) `Regions and Divisions` 行 81—90 同义核对；该页其他旧地理定义同样未用于现行都会规则 |
| [Census USPS City Versus Census Geography](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/usps_census_city.html)：邮寄 city / ZIP 与行政、统计地理不同 | 实读正文行 147—163，包括 Waterloo／Washburn 例子、physical location / geocode 及 USPS ZIP lookup。页修订 2026-02-04。正文没有把 ZCTA 写成行政界，也没有声称可凭 ZIP 确认学区 |
| [Census About Metropolitan and Micropolitan Statistical Areas](https://www.census.gov/programs-surveys/metro-micro/about.html)：都会门槛、县级组成、通勤、统计用途 | 完整主文行 150—180；现页修订 2026-02-27，采用 2020 standards、2023-07 OMB 划分。metro 至少一 urban area ≥50,000，micro 核心 ≥10,000 且 <50,000；不是整个都会区总人口，也不是简单市人口。核心县、外围县细项已读但正文未逐项展开；边界可变、非统计项目另问主管机关 |
| [Census Urban and Rural](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/urban-rural.html)：2020 城乡定义 | 行 147—149，densely settled core / density、非住宅相邻土地、≥2,000 housing units **or** ≥5,000 population；其余为 rural。公告区标注 2023-09 更新。没有把门槛当充分且唯一标准；没有沿用旧 2,500 人门槛 |
| [USDA ERS What Is Rural?](https://www.ers.usda.gov/topics/rural-economy-population/rural-classifications/what-is-rural)：metro／rural 交叉、项目定义 | 页更新 2026-02-09；完整主文行 88—140，重点 112—127 明确多数县兼有城乡、metro 含农村、nonmetro 含 urban。正文只用概念及项目选择定义，不引用人口总量、比例或趋势；原文行 107 的人口单位有明显排版错误，未采用 |
| [MBTA Trip Planner](https://www.mbta.com/trip-planner)：波士顿一带交通查询入口 | `web.open` restricted URL；同日普通 HTTPS `urllib.request.urlopen` TLS 校验开启得到 HTTP 200，BeautifulSoup `main` 实读 From / To / When / Now / Leave at / Arrive by / Modes / Commuter Rail / Subway / Bus / Ferry / Prefer accessible routes。未执行真实行程查询，不声称路线可用或覆盖全州 |
| [NJ TRANSIT Plan Your Trip](https://www.njtransit.com/trip-planner-to)：新泽西交通入口 | `web.open` 成功，实际 Plan Your Trip / System Status 与 Train & Light Rail、Bus、各线路和 Check All Alerts。页面行程部件由动态脚本加载，未编造具体输入步骤，正文仅链接入口 |
| [CTA Plan a Trip](https://www.transitchicago.com/planatrip/)：芝加哥交通入口 | 行 28—68，起终点、日期时间、Google Maps 以及 accessible / step-free 条件；并实际读到 current / upcoming alerts。只说明可从该官方入口开始查，没有声称交通规划器覆盖全州、班次或票价 |
| [Metro Rider Tools](https://www.wmata.com/ridertools)：华盛顿地区交通入口 | 原 `/schedules/trip-planner/` 自动转到该 URL，正文采用最终地址。主文行 0—60，maps / alerts / accessibility / elevators / parking、起终点与 Leave now、Options；不采用页面动态票价数字，也不把 Metro 覆盖当作 DC 行政界 |
| [Alaska Marine Highway Our Route](https://dot.alaska.gov/amhs/route.shtml)：海上路线与季节限制 | 主文 Our Route / Southeast / Southcentral / Southwest 行 38—103，尤其行 92：Kodiak / Ouzinkie / Port Lions year-round；该地区其他社区冬季受天气限制无渡轮。已读路线说明中的 **proposed winter 2026/27** 不去 Prince Rupert / Yakutat / cross gulf，不把提议班表写成确定未来状态。另读 [AMHS 首页](https://dot.alaska.gov/amhs/) 发现仍列 2025 / winter 2025—26 公告，因此正文不转述其旧班次，只引现行路线说明及按日期查班次的方法 |
| [Hawaii Airports System](https://airports.hawaii.gov/)：岛屿与具体机场 | 全页机场目录，HNL / OGG / ITO / KOA / LIH / MKK / LNY 等实际入口。正文只推荐据目录找机场，不声称所有岛有直航、航班频率、票价或岛际渡轮有无；候机／往返机场计入时间属于编辑比较方法 |
| [NOAA NCEI U.S. Climate Normals](https://www.ncei.noaa.gov/products/land-based-station/us-climate-normals)：长期气候比较 | 主文行 3—24：uniform 30-year、1991—2020、2021-05 v1.0.0，23 站 2023 重发 v1.0.1；Quick Access / Full Access、2006—2020 补充 15 年系列。实读下文站点历史均一化差异说明，但不做跨版本气候趋势算术。本站正在迁云且可能短暂数据延迟，本次产品说明可读；未下载站点数值、未宣称得到指定住址数据 |
| [NOAA 2022 Massachusetts](https://statesummaries.ncics.org/chapter/ma/) 与 [New Jersey](https://statesummaries.ncics.org/chapter/nj/)：东北州内差异 | MA Narrative 行 104—107：cold snowy winters / warm summers、东沿海平原与西部较高地形；NJ Narrative 行 105—109：冬夏、湿度、西北高地与东沿海、冬季温差。正文未引用升温排名、历史极端年或具体温度数量 |
| [NOAA 2022 Illinois](https://statesummaries.ncics.org/chapter/il/)：内陆、南北与湖泊 | Narrative 行 105—106：冬季北极冷气团、夏季暖湿气团、南北气温差、Lake Michigan 对东北部调节；不将芝加哥代表全州，也不把湖泊调节说成冬季暖和 |
| [NOAA 2022 Florida](https://statesummaries.ncics.org/chapter/fl/) 与 [Texas](https://statesummaries.ncics.org/chapter/tx/)：温暖地区内差与寒潮 | FL Narrative 行 99—108：hot humid summers / mild winters、January 南北差；TX Narrative 行 100—109：东西降水差、cold waves 等极端天气。具体地理背景适用，不推断 2026 某日状态，不给房屋供暖制冷法定标准 |
| [NOAA 2022 California](https://statesummaries.ncics.org/chapter/ca/) 与 [Washington](https://statesummaries.ncics.org/chapter/wa/)：海洋、内陆和山脉 | CA Narrative 行 99—101：沿海温和、内陆温差、高海拔低温重雪；WA Narrative 行 99—101：Cascades 西部较湿／东部少雨、东部温度年变化大。正文只用地理背景，不以 2022 文献支撑当前火情、雪封路或新政策 |
| [NOAA 2022 Alaska](https://statesummaries.ncics.org/chapter/ak/) 与 [Hawai‘i](https://statesummaries.ncics.org/chapter/hi/)：偏远背景与微气候 | AK Narrative 行 104—110：纬度、海拔、海洋、海冰、Interior 最大季节变化；HI Narrative 行 100—101、122—124：海拔温差、山地与 trade winds、迎风／背风短距离降雨差。未引用正文外照片、地图或图像，也未把 AK / HI 原住民社区写成单一经验 |
| [NIST Approximate Conversions](https://www.nist.gov/pml/owm/metric-si/unit-conversion/approximate-conversions-us-customary-measures-metric)：英里和华氏 | Length 行 138—145：mi × 1.61 ≈ km；Temperature exact 行 176—182：(°F − 32) / 1.8。32→0、68→20、86→30 为作者按该式算术，已核对；未误用温差公式 |
| [NIST Local Time FAQs](https://www.nist.gov/pml/time-and-frequency-division/local-time-faqs)：时区与 DST | 实读主文行 149—197。页创建 2024-09-16、更新 2024-10-11，2026-10-13 当前可访问；3 月第二周日／11 月第一周日、HI / 大多数 AZ / 所列属地例外、Navajo 例外、ST / DT / PT、跨国切换期不同、州县甚至跨区。AKT / HT 表说明 Aleutian 采用 DST、Hawaii 不采用。正文没有写固定中美时差或声称某提案已经生效 |
| [FCC How to Submit an Availability Challenge](https://help.bdc.fcc.gov/hc/en-us/articles/10476040597787-How-to-Submit-an-Availability-Challenge)：宽带地址核实与受阻入口 | 更新 2025-05-15；完整主文行 5—57，包括 provider-reported availability、非性能／价格、固定可用性异议、证据／核实邮箱／provider response。正文只用基本地图边界与不能安装时的正式入口；未承诺接通期限、程序胜诉或网络性能。真实申请、消费者联系、按钮操作均未执行 |
| [Census Comparing ACS Data](https://www.census.gov/programs-surveys/acs/guidance/comparing-acs-data.html)：同口径地区比较 | 主文行 154—187，sample estimates、MOE、1-year 只与 1-year、5-year 只与 5-year，跨期采用不重叠 5-year，变量和地理变化。已读 2020 experimental 1-year 不可与其他系列比的例外，但正文没有做这种比较，也未推荐该特殊数据。本文无真实地区人口、房租、收入、治安或学校评分数值 |

## 作者方法、演算与未确认项

- 地址、一周行程、工作岗位、房屋设备、费用与必要服务的清单是编辑整理的方法，不声称是某机构规定的申请条件。官方交通入口实际可读，但未运行任何私人地址行程或进行实地体验。
- 算例明确教学虚构：A = 2400 + 200 + 100 = 2700；B = 2000 + 250 + 800 = 3050；租金差 −400，总支出差 +350；(60 − 35) × 2 × 20 = 1000 分钟 = 16 小时 40 分钟。没有真实房源、报价或生活质量推断。
- 学区、租约、医疗、州税与驾驶的详细规则交由对应已存在主题解释，本页没有复制新资格或期限。DC 与 Tribal Nations 的主管框架引用既有政府稿；四 Census 区域不代替法域。
- 未核验具体住址的供水、宽带安装承诺、停车、租金、道路全年通行、渡轮／航班具体日期、真实通勤可靠性、学校学位、诊所是否接新病人、灾害概率、未来气候或保险价格。正文明确要按住址与日期继续查，未以“本州通常如此”填空。
- 不使用网页图片／截图／地图资产，只给文字释义与官方普通链接；没有下载或存放大原件。未构建、未改共享文件、未安装审阅元数据。

## 复核触发

- Census／OMB 发布新 urban criteria 或 metro delineations，或书内开始展示真实跨年统计：重核定义、地理版本、ACS 比较条件及所有衍生数字。
- NOAA 发布新 normals、修订站点数据或换州气候摘要版本：更新期间与入口；若新增实际数值或极端事件，另取相应原始数据，不机械沿用 2022 背景。
- DST／时区现行规则改变时，按生效法律及主管机构当前实施资料复核；不把议案新闻当现行变更。
- 交通机构规划器迁移、线路／季节服务变化、FCC 地图或异议说明修订：重新核正文实际使用的入口和行动边界。AMHS 2026/27 提议班表若被用于后续旅行页，须重新查正式班表。
- 后续要提出具体地区推荐、费用估计、班次承诺或学校／安全排名时，必须新增相应的地址、年份、来源与限制；本页的概念证据不能承接这些断言。
