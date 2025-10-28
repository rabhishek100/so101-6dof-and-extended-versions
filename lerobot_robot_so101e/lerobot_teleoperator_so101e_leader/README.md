# lerobot_teleoperator_so101e_leader

Leader teleoperator that mirrors the 7-DoF SO-101E follower arm.

## Installation

```bash
cd lerobot_teleoperator_so101e_leader
pip install -e .
```

The package prefix (`lerobot_teleoperator_`) makes `so101e_leader` available to
all LeRobot CLI tools.

## Usage

```bash
lerobot-teleoperate \
  --teleop.type=so101e_leader \
  --teleop.port=/dev/ttyUSB1
```

This leader reports `elbow_rotate.pos` in addition to the original SO-101
joints, so teleoperation policies can drive the extra DoF.

## Differences vs SO-101 leader

- Adds the elbow rotation motor using Feetech ID 4, keeping ids continuous
  between the leader and follower.
- Shares identical calibration/setup steps ensuring paired follower motion.
- Keeps feedback unsupported (same as upstream) while exposing the richer
  action space.
