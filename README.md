# robosim_library
update:2026.0314

這個倉庫提供 [RoboSim](https://avery320.github.io/robot-demo/javascript/example/bundle/main.html) 的基礎機械手臂模型檔。

## Library Metadata

每個模型目錄都應包含一份 `model.json`，作為唯一資料來源。內容包括：

```json
{
  "id": "abb_irb1200",
  "label": "ABB / IRB1200",
  "vendor": "ABB",
  "model": "IRB1200",
  "urdf": "library/abb/abb_irb1200/urdf/abb_irb1200.urdf",
  "author": "Avery Tsai",
  "source": "ros-industrial/abb"
}
```

## index.json 

`library/index.json` 是由各模型的 `model.json` 自動生成，不應手動編輯，現**階段先以 python 腳本進行手動更新**。

```bash
python3 scripts/generate_index.py
```


## Robot URDF
以下為從開源專案獲取 urdf 模型的方法。

### [UR robot](https://github.com/UniversalRobots/Universal_Robots_ROS2_Description.git)

```bash
rosrun xacro xacro --inorder ur.urdf.xacro ur_type:=ur5 name:=ur > ur5.urdf #name:=<robot name>
```

### [ABB robot](https://github.com/ros-industrial/abb.git)

```bash
rosrun xacro xacro irb1200_5_90.xacro > abb_irb1200.urdf
```

### [KUKA robot](https://github.com/kroshu/kuka_robot_descriptions.git)

#### 修正 mesh 路徑
```bash
sed -i.bak 's|package://abb_irb1200_support/meshes|../meshes|g' abb_irb1200.urdf
```
