# coding: utf-8
#
# Copyright 2020 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Definition of platform parameters."""

from __future__ import annotations

import enum

from core.domain import platform_parameter_domain
from core.domain import platform_parameter_registry as registry

Registry = registry.Registry


class ParamNames(enum.Enum):
    """Enum for parameter names."""

    DUMMY_FEATURE = 'dummy_feature'
    DUMMY_PARAMETER = 'dummy_parameter'

    END_CHAPTER_CELEBRATION = 'end_chapter_celebration'
    CHECKPOINT_CELEBRATION = 'checkpoint_celebration'
    CONTRIBUTOR_DASHBOARD_ACCOMPLISHMENTS = (
        'contributor_dashboard_accomplishments')
    ANDROID_BETA_LANDING_PAGE = 'android_beta_landing_page'
    BLOG_PAGES = 'blog_pages'
    DIAGNOSTIC_TEST = 'diagnostic_test'
    SERIAL_CHAPTER_LAUNCH_CURRICULUM_ADMIN_VIEW = (
        'serial_chapter_launch_curriculum_admin_view')
    SHOW_TRANSLATION_SIZE = 'show_translation_size'

    PROMO_BAR_ENABLED = 'promo_bar_enabled'
    PROMO_BAR_MESSAGE = 'promo_bar_message'


# Platform parameters should all be defined below.

Registry.create_feature_flag(
    ParamNames.DUMMY_FEATURE,
    'This is a dummy feature flag.',
    platform_parameter_domain.FeatureStages.DEV,
)

Registry.create_platform_parameter(
    ParamNames.DUMMY_PARAMETER,
    'This is a dummy platform parameter.',
    platform_parameter_domain.DataTypes.STRING
)

Registry.create_feature_flag(
    ParamNames.END_CHAPTER_CELEBRATION,
    'This flag is for the end chapter celebration feature.',
    platform_parameter_domain.FeatureStages.PROD,
)

Registry.create_feature_flag(
    ParamNames.CHECKPOINT_CELEBRATION,
    'This flag is for the checkpoint celebration feature.',
    platform_parameter_domain.FeatureStages.PROD,
)

Registry.create_feature_flag(
    ParamNames.CONTRIBUTOR_DASHBOARD_ACCOMPLISHMENTS,
    'This flag enables showing per-contributor accomplishments on the' +
    ' contributor dashboard.',
    platform_parameter_domain.FeatureStages.PROD,
)

Registry.create_feature_flag(
    ParamNames.ANDROID_BETA_LANDING_PAGE,
    'This flag is for Android beta promo landing page.',
    platform_parameter_domain.FeatureStages.PROD)

Registry.create_feature_flag(
    ParamNames.BLOG_PAGES,
    'This flag is for blog home page, blog author profile page and blog post' +
    ' page.',
    platform_parameter_domain.FeatureStages.PROD)


Registry.create_feature_flag(
    ParamNames.DIAGNOSTIC_TEST,
    'This flag is for the diagnostic test functionality.',
    platform_parameter_domain.FeatureStages.PROD)

Registry.create_feature_flag(
    ParamNames.SERIAL_CHAPTER_LAUNCH_CURRICULUM_ADMIN_VIEW,
    'This flag is for serial chapter launch feature and making changes only' +
    'in the curriculum admin view.',
    platform_parameter_domain.FeatureStages.DEV)

Registry.create_feature_flag(
    ParamNames.SHOW_TRANSLATION_SIZE,
    'This flag is to show translation size on translation cards in' +
    'contributor dashboard.',
    platform_parameter_domain.FeatureStages.DEV)

Registry.create_platform_parameter(
    ParamNames.PROMO_BAR_ENABLED,
    'Whether the promo bar should be enabled for all users',
    platform_parameter_domain.DataTypes.BOOL
)

Registry.create_platform_parameter(
    ParamNames.PROMO_BAR_MESSAGE,
    'The message to show to all users if the promo bar is enabled',
    platform_parameter_domain.DataTypes.STRING
)
