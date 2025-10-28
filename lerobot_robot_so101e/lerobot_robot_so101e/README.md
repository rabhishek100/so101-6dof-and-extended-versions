# lerobot_robot_so101e

Third-party LeRobot plugin that exposes the SO-101E follower: a SO-101 arm
augmented with an elbow-rotation servo for 7-DoF manipulation.

## Installation

```bash
cd lerobot_robot_so101e
pip install -e .
```

Installing the package makes it discoverable by `lerobot` thanks to the
`lerobot_robot_` prefix, and it registers the `so101e_follower` config.

## Usage

```bash
lerobot-record \
  --robot.type=so101e_follower \
  --robot.port=/dev/ttyUSB0
```

The follower exposes the same observation/action contract as the stock SO-101,
but adds `elbow_rotate.pos` to both streams.

## Differences vs SO-101

- Adds a seventh motor (`elbow_rotate`) wired to Feetech ID 4 by default.
- Motor IDs stay contiguous (1–7), so setup steps match the default SO-101
  ordering with the elbow rotation inserted after `elbow_flex`.
- Shares the same calibration, connection, and safety flows as the upstream
  implementation so existing tooling keeps working.
