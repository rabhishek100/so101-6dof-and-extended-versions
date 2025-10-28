#!/usr/bin/env python

# Copyright 2025 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from dataclasses import dataclass, field

from lerobot.cameras import CameraConfig
from lerobot.robots.config import RobotConfig


@RobotConfig.register_subclass("so101e_follower")
@dataclass
class SO101EFollowerConfig(RobotConfig):
    """
    Configuration for the SO-101E follower arm.

    It extends the stock SO-101 by adding a seventh motor that rotates the elbow,
    enabling compound wrist poses without contorting the shoulder.
    """

    # Serial port used by the Feetech bus.
    port: str

    disable_torque_on_disconnect: bool = True

    # Cap on the delta between measured and commanded joint targets.
    max_relative_target: float | dict[str, float] | None = None

    # Optional USB / CSI cameras mounted on the follower.
    cameras: dict[str, CameraConfig] = field(default_factory=dict)

    # Old datasets/policies use degrees, newer pipelines expect [-100, 100] normalized units.
    use_degrees: bool = False
