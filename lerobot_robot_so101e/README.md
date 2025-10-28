# SO-101E 7-DoF Plugins

This repository hosts the third-party LeRobot plugins that describe the
SO-101E hardware variant—a SO-101 follower/leader pair with an additional
elbow-rotation servo.

## Layout

- `lerobot_robot_so101e`: robot plugin exposing `so101e_follower`.
- `lerobot_teleoperator_so101e_leader`: teleoperator plugin exposing
  `so101e_leader`.
- `lerobot`: shallow clone of the upstream project used for reference only.

## Installing

Install each package in editable mode while developing:

```bash
pip install -e lerobot_robot_so101e
pip install -e lerobot_teleoperator_so101e_leader
```

Both names follow the prefixes recommended in the
[Bring Your Own Hardware](https://huggingface.co/docs/lerobot/integrate_hardware)
guide, so the LeRobot CLI auto-discovers them.

## Quick Usage

```bash
lerobot-record --robot.type=so101e_follower --robot.port=/dev/ttyUSB0
lerobot-teleoperate --teleop.type=so101e_leader --teleop.port=/dev/ttyUSB1
```

Both devices assume the extra elbow servo sits on Feetech ID 4, keeping ids
continuous from 1 through 7.
