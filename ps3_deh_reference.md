# PS3 DEH (Debugging Station) NID Reference

Quick reference of NIDs from this repo relevant to DECH-3000 / DEH hardware.
All data sourced from `ps3_names.txt` and `ps3.xml` in this repository — organized by category.

## DEH Detection (cellSsAim*)

| NID | Function | Description |
|-----|----------|-------------|
| `0x1F80E287` | `cellSsAimIsDEH` | Detect DECH-3000 Debugging Station |
| `0xC0E39B97` | `cellSsAimIsDEHA` | Detect DEH-A variant |
| `0xE4A68606` | `cellSsAimIsDEHXB` | Detect DEH-XB variant |
| `0xE35D54E3` | `cellSsAimIsDEHXB2` | Detect DEH-XB2 variant |
| `0x8AD55D80` | `cellSsAimIsDEX` | Detect Development Kit |
| `0x0F48562D` | `cellSsAimIsCEX` | Detect Consumer/Retail unit |
| `0x145991B4` | `cellSsAimIsARCADE` | Detect Arcade unit |
| `0x8F71C2DF` | `cellSsAimGetDeviceType` | Get hardware type enum |
| `0x3B4A1AC4` | `cellSsAimGetDeviceId` | Get unique device identifier |
| `0x9AD2E524` | `cellSsAimGetOpenPSID` | Get OpenPSID |
| `0x3F062337` | `cellSsAimChkregPsCode` | Check region PS code |

## Security Syscalls

| Syscall | Function | Description |
|---------|----------|-------------|
| 8 | `sys_process_authenticate_program_segment` | SELF/SPRX authentication |
| 470 | `sys_npdrm_check_ekc` | NP DRM EKC check |
| 471 | `sys_npdrm_regist_ekc` | NP DRM EKC registration |
| 976 | `sys_crypto_engine_create` | Create crypto engine context |
| 977 | `sys_crypto_engine_destroy` | Destroy crypto engine context |
| 978 | `sys_crypto_engine_hasher_prepare` | Prepare hash operation |
| 979 | `sys_crypto_engine_hasher_run` | Execute hash operation |
| 980 | `sys_crypto_engine_hasher_get_hash` | Retrieve hash result |
| 981 | `sys_crypto_engine_cipher_prepare` | Prepare cipher operation |
| 982 | `sys_crypto_engine_cipher_run` | Execute cipher operation |
| 983 | `sys_crypto_engine_cipher_finish` | Finalize cipher operation |
| 984 | `sys_crypto_engine_random_generate` | Generate random bytes |
| — | `proc_decrypt_lv2_self` (0x00010042) | Decrypt LV2 SELF binary |

## Vault / Secure Storage (cellSsVtrm*)

| NID | Function | Description |
|-----|----------|-------------|
| `0xA79070D5` | `cellSsVtrmDecrypt` | Decrypt vault data |
| `0x3231E012` | `cellSsVtrmDecryptMaster` | Decrypt with master key |
| `0x4FD63C1D` | `cellSsVtrmEncrypt` | Encrypt vault data |

## Update Manager (cellSsUm* / ss::update_manager_if)

| Symbol | Function | Description |
|--------|----------|-------------|
| — | `ss::update_manager_if::is_product_mode` | Check DEX/CEX mode |
| — | `ss::update_manager_if::get_token_seed` | Get update token seed |
| — | `cellSsUmReadEprom` | Read EPROM |
| — | `cellSsUmWriteEprom` | Write EPROM |
| — | `cellSsUmGetCacheOfProductMode` | Cached product mode |
| — | `cellSsUmExtractPackage` | Extract update package |
| — | `cellSsUmUpdatePackage` | Apply update package |
| — | `cellSsUmGetTokenSeed` | Get token seed |
| — | `cellSsUmInspectPackage` | Inspect update package |

## Crypto Primitives (cellCryptoPu*)

51 functions covering:
- **AES**: CBC, CFB-128, OMAC1
- **RSA**: 512/1024/2048-bit sign, verify, encrypt
- **ECDSA/ECDH**: Sign, verify, key agreement
- **SHA**: SHA-1, SHA-256, HMAC variants
- **TDES**: Triple DES
- **PRNG**: FIPS-186 compliant

## Unresolved NIDs

~20 `avc_util_*` entries in `ps3.xml` where `name == hash` — candidates for reversing on DEH hardware.

## Sources

All NIDs verified against `ps3.xml` and `ps3_names.txt` in this repository.
