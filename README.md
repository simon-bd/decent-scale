# 🏋️‍♂️ Decent Scale – Home Assistant Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=flat-square)](https://hacs.xyz/docs/faq/custom_repositories)

This is a custom [Home Assistant](https://www.home-assistant.io/) integration for the **Decent Scale** by [Decent Espresso](https://decentespresso.com/), bringing **real-time weight tracking** and control into your smart home setup — perfect for espresso shot automation!

## ☕ Features

- Real-time weight sensor
- Stability indicator (coming soon)
- Live updates via Bluetooth
- Tare and timer button support (planned)

## 🚀 Installation

1. In Home Assistant, go to **HACS > Integrations > 3 dots (⋮) > Custom repositories**.
2. Add this repo:  
   `https://github.com/simon-bd/decent-scale`  
   Category: **Integration**
3. Search for "Decent Scale" in HACS and install.
4. Restart Home Assistant.

> **Note**: Requires [Bluetooth Proxy via ESPHome](https://esphome.io/components/bluetooth_proxy.html) or native Bluetooth.

## ⚙️ Configuration

Currently, this integration is auto-loaded by Home Assistant. Configuration is minimal and will be expanded with UI support later.

## 🧠 Powered By

- [`pydecentscale`](https://github.com/lucapinello/pydecentscale) – Python library for interacting with the scale
- Home Assistant's custom component platform

## 💡 Ideas / Contributions

- Add config flow and options
- Improve update frequency for ultra-low latency
- Add support for multiple scales

## 🛠️ License

MIT

---

Built with ❤️ by [Simon](https://github.com/simon-bd)
