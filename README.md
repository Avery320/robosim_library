# robosim_library

這個倉庫提供 [RoboSim](https://avery320.github.io/robot-demo/javascript/example/bundle/main.html) 的基礎機械手臂模型檔，新增模型會自動加入 [RoboSim](https://avery320.github.io/robot-demo/javascript/example/bundle/main.html) 的 Robot Library 中。

## 開發規範

本專案採用以下 ROS 座標與框架慣例作為開發標準：

- [**ROS REP-103**](https://www.ros.org/reps/rep-0103.html)：通用單位與座標規範
- [**ROS REP-199**](https://gavanderhoorn.github.io/rep/rep-0199.html)：串聯式工業機械手臂之座標框架語意規範

所有貢獻者在開發或更新機器人描述、座標階層、flange／tool 定義，以及相關運動學資料時，應參考上述規範。


## 目前收錄的機械手臂

<!-- ROBOT_TABLE_START -->
| 出廠 | ID | Author | Source |
|------|----|--------|--------|
| ABB | `abb_crb15000` | Avery Tsai | abb |
| ABB | `abb_irb120` | Avery Tsai | abb |
| ABB | `abb_irb1200` | Avery Tsai | abb |
| ABB | `abb_irb4600` | Avery Tsai | abb |
| KUKA | `kuka_kr16_r1610_2` | Avery Tsai | kuka_robot_descriptions |
| KUKA | `kuka_kr240_r3330` | Avery Tsai | kuka_robot_descriptions |
| KUKA | `kuka_kr300_r2700_2` | Avery Tsai | kuka_robot_descriptions |
| KUKA | `kuka_kr560_r3100_2` | Avery Tsai | kuka_robot_descriptions |
| KUKA | `kuka_lbr_iiwa14_r820` | Avery Tsai | kuka_robot_descriptions |
| KUKA | `rccn_kuka_kr300r2500` | Avery Tsai | kuka_kr300_support |
| UR | `ur10` | Avery Tsai | Universal_Robots_ROS2_Description |
| UR | `ur16e` | Avery Tsai | Universal_Robots_ROS2_Description |
| UR | `ur5` | Avery Tsai | Universal_Robots_ROS2_Description |
<!-- ROBOT_TABLE_END -->

