# B05 地区生活比较独立事实审

- 日期：2026-10-13。
- 作者：health；独立事实审：civic；第三人静态审由 root 另做。
- 正文：`content/book/foundations/geography/regional-life.md`。
- 结论：**PASS**。未发现需修订的实质事实问题。审者未修改正文、作者证据或共享文件，未构建。
- 绑定正文 SHA-256：`aa982155b6b883ca880b8a025e02a2339e834d856e50ea0b29f0e3fbca3461d9`。
- 算法：全文按 `split('---',2)[2]` 取正文，UTF-8 后 SHA-256；开始与完成时实际文件均匹配。

## 独立回源

作者地图与证据只用来定位待查断言。以下来源均由审者另行访问原文并核对，未用作者记录代替阅读。网页行号是本轮工具提取位置；遇到 web 间歇失败时，普通 HTTPS requests 保持 TLS 校验并读取实际正文。

| 正文范围 | 审者实际来源与定位 | 核对结果 |
|---|---|---|
| 四区域、九分区、各州与 DC 例子 | [Census Geographic Levels](https://www.census.gov/programs-surveys/economic-census/guidance-geographies/levels.html)，Regions and Divisions，L278–295 | 逐一核对 MA New England、NY/NJ Middle Atlantic、IL Midwest、TX/FL/DC South、CA/WA/AK/HI Pacific；均相符。仅用该页区域清单，未取其旧Economic Census都会定义。 |
| 邮寄城市、ZIP 与实际地方 | [Census USPS City Versus Census Geography](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/usps_census_city.html)，L147–158，Waterloo及Washburn例子 | 机构明确按住宅实际地理定位，而非postal city；邮政名可跨市界，学校与其他服务另查的正文方法成立。未把ZCTA当行政界。 |
| 都会统计区、micro、核心门槛与2023划分 | [Census About Metropolitan and Micropolitan Statistical Areas](https://www.census.gov/programs-surveys/metro-micro/about.html)，普通HTTPS200全文；Delineating与Uses部分，页修订2026-02-27 | 现2020 standards、2023-07 OMB划分；metro至少一urban area≥50,000，micro≥10,000且<50,000；县或同级为组成单位、外围通勤联系、统计用途均吻合。web再次请求失败后直接读取同URL实际原文。 |
| 2020 urban/rural | [Census Urban and Rural](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/urban-rural.html)，L147–149、2023-09公告 | 至少2,000 housing units或5,000人口是在满足密度／相邻地块等划界标准之后的要求；稿件未把行政市总人口当urban充分条件，未用旧2,500门槛。 |
| 都会县含乡村、非都会含城镇、项目自选定义 | [USDA ERS What Is Rural?](https://www.ers.usda.gov/topics/rural-economy-population/rural-classifications/what-is-rural)，L88–102、112–138 | 两套地理模型会交叉；正文正确引导读者回到具体项目地址资格。审者不采用来源L107的明显“人数million”排版错误。 |
| ACS比较 | [Census Comparing ACS Data](https://www.census.gov/programs-surveys/acs/guidance/comparing-acs-data.html)，普通HTTPS200，完整主文；页修订2026-01-23 | ACS为样本估计并有MOE；1-year/5-year同类比较，不重叠5年期间、变量和边界变化相符。文中未使用2020 experimental 1-year或任何实际地区数值，没有遗漏影响本稿算例的特殊年份。 |
| 气候常年值版本与用途 | [NOAA NCEI U.S. Climate Normals](https://www.ncei.noaa.gov/products/land-based-station/us-climate-normals)，L3–24 | 当前标准1991–2020，补充2006–2020；monthly等站点资料可查询。当前迁云／间歇下载延迟提示存在，但说明页实读；正文未声称已得到某住址观测数值或数据下载永远可用。 |
| MA与NJ气候 | [NOAA 2022 MA](https://statesummaries.ncics.org/chapter/ma/) L104–107；[NOAA 2022 NJ](https://statesummaries.ncics.org/chapter/nj/) L105–109 | MA冬冷多雪、沿海与西部地形；NJ西北高地较冷、冬季沿海差异均吻合，只作为2022长期地理背景。 |
| IL气候 | [NOAA 2022 IL](https://statesummaries.ncics.org/chapter/il/)，L105–106 | 南北温差、Lake Michigan对东北部的调节与正文一致；没有推导全州相同天气或服务。 |
| FL与TX气候 | [NOAA 2022 FL](https://statesummaries.ncics.org/chapter/fl/) L99–102；[NOAA 2022 TX](https://statesummaries.ncics.org/chapter/tx/) L100–102 | FL湿热夏季温和冬季及冬温南北差；TX东西降水差及cold waves均原文可见。设备核对清单是编辑建议，未伪装成住房法规。 |
| CA与WA气候 | [NOAA 2022 CA](https://statesummaries.ncics.org/chapter/ca/) L99–101；[NOAA 2022 WA](https://statesummaries.ncics.org/chapter/wa/) L99–101 | CA沿海海洋调节、内陆温差、高海拔低温雪；WA Cascades东西降水／温度年变化均吻合，未据此给当前道路状态。 |
| AK与HI气候 | [NOAA 2022 AK](https://statesummaries.ncics.org/chapter/ak/) L104–110；[NOAA 2022 HI](https://statesummaries.ncics.org/chapter/hi/) L100–101、122–124 | AK海洋／北极／内陆季节差；HI海拔和迎背风坡导致短距离差异；均在正文适用范围内。 |
| 英里与温度 | [NIST Approximate Conversions](https://www.nist.gov/pml/owm/metric-si/unit-conversion/approximate-conversions-us-customary-measures-metric)，Length L138–145、Temperature exact L176–182 | 英里约1.61公里；(F−32)/1.8准确，三个示例独立演算为0、20、30°C。 |
| 时区和DST | [NIST Local Time FAQs](https://www.nist.gov/pml/time-and-frequency-division/local-time-faqs)，L149–197，更新2024-10-11、当前实读 | 3月第二周日、11月第一周日、HI和多数AZ不采用、Navajo例外、PST/PDT/PT、不同国家切换日期等吻合。只凭州名不足以确定时区的提醒有州县跨区原文支持。 |
| MBTA入口 | [MBTA Trip Planner](https://www.mbta.com/trip-planner)，普通HTTPS200，实际main正文 | 读到From/To、When、Leave at/Arrive by、各模式和Prefer accessible routes。未替私人地址运行行程；只能确认入口，与正文范围相同。 |
| NJ TRANSIT入口 | [Plan Your Trip](https://www.njtransit.com/trip-planner-to)，L151以下及官方菜单 | 当前Plan Your Trip、System Status、train/light rail/bus和alerts；正文未编造动态规划器结果、票价或班次。 |
| CTA入口 | [CTA Plan a Trip](https://www.transitchicago.com/planatrip/)，L28–83 | 输入起终点、日期、时间、accessible/step-free以及Google Maps入口实读；只确认其功能用途，不验证实际路线或全州覆盖。 |
| WMATA入口 | [Metro Rider Tools](https://www.wmata.com/ridertools)，L2–15、45–60 | 起终点、Leave now/Options、maps、alerts、elevators等可读；正文正确称华盛顿地区而非华盛顿州或DC行政边界。 |
| 阿拉斯加季节渡轮 | [AMHS Our Route](https://dot.alaska.gov/amhs/route.shtml)，L38–43、77–103 | 西南Kodiak/Ouzinkie/Port Lions全年，其余部分社区冬季天气限制原文明确。页面另写proposed winter2026/27，稿件未把提案航线写成已执行班次；按日期另查的范围正确。 |
| 夏威夷机场 | [Hawaii Airports System](https://airports.hawaii.gov/)，L9–37机场目录 | HNL/OGG/ITO/KOA/LIH/MKK/LNY等入口存在；正文只要求具体岛屿、机场与候机交通时间，不给全岛直航或班次承诺。 |
| 宽带地图与异议 | [FCC Availability Challenge](https://help.bdc.fcc.gov/hc/en-us/articles/10476040597787-How-to-Submit-an-Availability-Challenge)，更新2025-05-15，L5–24、28–57全文实读 | 地图为运营商报送的availability，不是实测性能／可负担性；未能接通可提challenge的相应原因存在。正文未把10 business days统计定义写成强制给申请人安装的期限，未承诺胜诉或安装。 |

## 内容边界与演算

- 地图、地区、都会和城乡用于比较背景；最终核对完整地址、具体服务机构、日期与日程。没有从区域／都会名推导税、学校、待遇或司法资格，也没有将DC当普通州或Tribal Nations列为县下级。
- 通勤、就业、服务距离、房屋设备、预算与亲友支持清单属于公开可用的比较方法，不声称是某政府的资格条件。对“早高峰有车不代表晚班有车”等仅作核对建议；并未列真实班次。
- 教学虚构算例独立演算：2400+200+100=2700；2000+250+800=3050；租金差−400，总计差+350；(60−35)×2×20=1000分钟=16小时40分钟。明确只有三项，不当完整家庭预算或地区报价。
- 正文全部内部链接实际目标文件存在。交通、学区、医保、租房、州税细节由其他主题承接，本次未替这些全页重新做事实审。
- 未核验真实地址的宽带订单、医生接诊、学校学位、灾害概率、交通可达性、道路或航班未来执行；正文也未作相应事实承诺。

## 后续

无作者返修项。root 仍需第三人静态审、候选元数据、构建与实际渲染；本PASS不能替代这些步骤。正文任何改变应重算SHA，按变化范围复核并重新绑定。
