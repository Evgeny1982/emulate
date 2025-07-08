# Barcode Scanner Emulator

Этот проект эмулирует поведение USB-сканера штрихкодов. Каждые 3 секунды он "вводит" в систему случайную игральную карту (например, `10H`, `AS`, `QD`), как будто она была считана сканером.

## Установка

```bash
sudo apt install python3-uinput
pip install -r requirements.txt
sudo modprobe uinput
