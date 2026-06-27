# CaramOS release/version bump tracker

Tài liệu này ghi lại các vị trí cần kiểm tra khi bump release CaramOS/OTA.
Mốc hiện tại: **CaramOS/Open Beta 1.0.11**.

> Quy ước: không phải mọi dòng `1.0.1` đều cần đổi. `1.0.1` vẫn là base ISO/Open Beta và là điểm bắt đầu migration chain.

## Cần đổi ngay cho OTA 1.0.11

| Trạng thái | File | Dòng/nhóm | Giá trị hiện tại | Cần đổi/kiểm tra |
|---|---|---|---|---|
| DONE | [README.md](../README.md) | badge/tổng quan release | `1.0.11` | đã đổi thành current version, không tách dòng OTA riêng |
| DONE | [README.md](../README.md) | mô tả migration chain | `1.0.11` | đã mô tả ISO build ra latest; OTA chỉ nâng máy cũ |
| DONE | [README_EN.md](../README_EN.md) | release badge | `1.0.11` | đã đổi thành current version, không tách dòng OTA riêng |
| DONE | [README_EN.md](../README_EN.md) | ordered migration chain example | `1.0.11` | đã mô tả ISO build ra latest; OTA chỉ nâng máy cũ |
| DONE | [scripts/config.sh](../scripts/config.sh) | `CARAMOS_VERSION_PATCH=11` | ISO release version `1.0.11` | đã bump source-of-truth cho ISO/tag |
| DONE | [scripts/config.sh](../scripts/config.sh) | comment ví dụ | `1.0.11` | đã cập nhật ví dụ tag |
| DONE | [landing/src/main.jsx](../landing/src/main.jsx) | release notes data | `1.0.11` | đã thêm release note `1.0.11` |
| DONE | [landing/src/main.jsx](../landing/src/main.jsx) | headline/copy version | `1.0.11` | đã bump hero/SEO/download copy |

## Đã cập nhật cho OTA 1.0.11

| Trạng thái | File | Nội dung |
|---|---|---|
| DONE | [packages/caramos-ota/debian/changelog](../packages/caramos-ota/debian/changelog) | top entry `1.0.11-0caramos1` |
| DONE | [packages/caramos-ota/usr/lib/python3/dist-packages/caramos_ota/constants.py](../packages/caramos-ota/usr/lib/python3/dist-packages/caramos_ota/constants.py) | `TOOL_VERSION = "1.0.11-0caramos1"` |
| DONE | [packages/caramos-ota/usr/lib/python3/dist-packages/caramos_ota_update/migrations/migration.json](../packages/caramos-ota/usr/lib/python3/dist-packages/caramos_ota_update/migrations/migration.json) | added `1.0.11` target |
| DONE | [packages/caramos-ota/usr/lib/python3/dist-packages/caramos_ota_update/migrations/v1_0_11/manifest.json](../packages/caramos-ota/usr/lib/python3/dist-packages/caramos_ota_update/migrations/v1_0_11/manifest.json) | new release manifest |
| DONE | [packages/caramos-ota/usr/lib/python3/dist-packages/caramos_ota_update/migrations/v1_0_11/fix_live_user_detection.py](../packages/caramos-ota/usr/lib/python3/dist-packages/caramos_ota_update/migrations/v1_0_11/fix_live_user_detection.py) | `1.0.10 -> 1.0.11` migration |

## Stale OTA documentation still mentioning 1.0.5

Các file này có nhiều hướng dẫn release cũ `1.0.5`. Nên sửa dần hoặc chuyển thành template generic để khỏi stale tiếp.

| File | Nội dung đã cập nhật |
|---|---|
| [packages/README.md](../packages/README.md) | release hiện tại `caramos-ota 1.0.11`, chain tới `1.0.11`, command upload `1.0.11-0caramos1` |
| [packages/caramos-ota/README.md](../packages/caramos-ota/README.md) | quy trình release OTA đến `1.0.11`, latest target `1.0.11`, ISO `1.0.11` |
| [packages/caramos-ota/README_EN.md](../packages/caramos-ota/README_EN.md) | release workflow through `1.0.11`, publish package `1.0.11-0caramos1` |

## Không nên đổi tự động

| File | Version | Lý do giữ |
|---|---|---|
| [install-caramos-ota.sh](../install-caramos-ota.sh) | fallback `1.0.1` | đây là metadata bootstrap cho máy ISO 1.0.1 trước khi OTA nâng lên latest |
| [scripts/config.sh](../scripts/config.sh) | `CARAMOS_MIGRATION_BASE_VERSION="1.0.1"` | base để build ISO chạy đủ migration chain từ đầu |
| [packages/caramos-ota/usr/lib/python3/dist-packages/caramos_ota_update/migrations/v1_0_2/manifest.json](../packages/caramos-ota/usr/lib/python3/dist-packages/caramos_ota_update/migrations/v1_0_2/manifest.json) | `from_version: 1.0.1` | migration lịch sử, không đổi |
| [packages/caramos-ota/usr/lib/python3/dist-packages/caramos_ota_update/migrations/v1_0_2/baseline.py](../packages/caramos-ota/usr/lib/python3/dist-packages/caramos_ota_update/migrations/v1_0_2/baseline.py) | `FROM_VERSION = "1.0.1"` | migration lịch sử, không đổi |
| [packages/caramos-ota/usr/lib/python3/dist-packages/caramos_ota_update/migrations/v1_0_10/*](../packages/caramos-ota/usr/lib/python3/dist-packages/caramos_ota_update/migrations/v1_0_10/) | `1.0.10` | migration lịch sử, giữ nguyên |
| [packages/caramos-ota/usr/lib/python3/dist-packages/caramos_ota_update/migrations/v1_0_11/*](../packages/caramos-ota/usr/lib/python3/dist-packages/caramos_ota_update/migrations/v1_0_11/) | `from_version: 1.0.10` | cạnh migration đúng cho `1.0.10 -> 1.0.11` |

## Quy trình scan lần sau

1. Scan latest cũ và latest mới trong repo, tránh `build/`, `cache/`, `output/`, package staging `debian/caramos-ota/`.
2. Phân loại kết quả thành:
   - release metadata cần đổi,
   - docs/landing cần đổi,
   - migration lịch sử không đổi,
   - bootstrap/base version không đổi.
3. Sau khi bump OTA:
   - cập nhật `debian/changelog`,
   - thêm version vào `migration.json`,
   - thêm `vX_Y_Z/manifest.json`, `__init__.py`, migration `.py`,
   - bump `caramos_ota/constants.py`,
   - build/upload PPA,
   - cập nhật README/landing/release note.
