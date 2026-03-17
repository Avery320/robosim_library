# robosim_library

這個倉庫提供 [RoboSim](https://avery320.github.io/robot-demo/javascript/example/bundle/main.html) 的基礎機械手臂模型檔，新增模型會自動加入 [RoboSim](https://avery320.github.io/robot-demo/javascript/example/bundle/main.html) 的 Robot Library 中。

## 開發規範

本專案採用以下 ROS 座標與框架慣例作為開發標準：

- [**ROS REP-103**](https://www.ros.org/reps/rep-0103.html)：通用單位與座標規範
- [**ROS REP-199**](https://gavanderhoorn.github.io/rep/rep-0199.html)：串聯式工業機械手臂之座標框架語意規範

所有貢獻者在開發或更新機器人描述、座標階層、flange／tool 定義，以及相關運動學資料時，應參考上述規範。


## 目前收錄的機械手臂

| 出廠 | 模型 | ID | Author |
|------|------|----|------|
| ABB | CRB15000 | `abb_crb15000` | Avery |
| ABB | IRB120 | `abb_irb120` | Avery |
| ABB | IRB1200 | `abb_irb1200` | Avery |
| ABB | IRB4600 | `abb_irb4600` | Avery |
| KUKA | KR16 R1610-2 | `kuka_kr16_r1610_2` | Avery |
| KUKA | KR240 R3330 | `kuka_kr240_r3330` | Avery |
| KUKA | KR300 R2700-2 | `kuka_kr300_r2700_2` | Avery |
| KUKA | KR560 R3100-2 | `kuka_kr560_r3100_2` | Avery |
| KUKA | LBR IIWA14 | `kuka_lbr_iiwa14_r820` | Avery |
| KUKA | KR300R2500 | `rccn_kuka_kr300r2500` | Avery |
| UR | UR5 | `ur5` | Avery |
| UR | UR10 | `ur10` | Avery |
| UR | UR16e | `ur16e` | Avery |

