#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client',
    'hardware/samsung',
    'vendor/samsung/a32'
]

blob_fixups: blob_fixups_user_type = {
    ('vendor/bin/hw/android.hardware.media.c2@1.2-mediatek', 'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b'): blob_fixup()
        .add_needed('libstagefright_foundation-v33.so'),
    ('vendor/bin/hw/vendor.samsung.hardware.camera.provider@4.0-service_64': blob_fixup()
        .replace_needed('libbinder.so', 'libbinder-v31.so')
        .replace_needed('libhidlbase.so', 'libhidlbase-v31.so')
        .replace_needed('libutils.so', 'libutils-v31.so'),
    'vendor/bin/hw/vendor.samsung.hardware.hyper-service': blob_fixup()
        .replace_needed('liblog.so', 'liblog-v31.so'),
    ('vendor/lib*/sensors.inputvirtual.so', 'vendor/lib*/sensors.sensorhub.so'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v31.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'a32',
    'samsung',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
