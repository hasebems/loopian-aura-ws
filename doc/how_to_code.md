# 本 Workshop でのプログラムの書き方

本日私は、マイコンボードと６つの NeoPixel が繋がっている Aura という電子基板を使って、プログラムを書き込み、いろいろなパターンで光らせようとしています。
今回使用するボードは MicroPython で動作するマイコンボード「Waveshare RP2040-Zero」(RP2040搭載)です。開発環境は Thonny を使用します。以下の情報を踏まえて Aura 向けのプログラムを書いてください。

## Aura のハードウェア構成
- フルカラーLED(NeoPixel/WS2812系)が6個、GPIO26番ピンに接続されている
- 各LEDは RGBW(4要素)形式で色を指定する

## 必要なインポート文
```python
import neopixel
from machine import Pin
import time
```

## 使用ライブラリ
- `neopixel.NeoPixel(Pin(26), 6, bpp=4)` でLEDを初期化する
  - 第1引数: 接続ピン(Pin(26))
  - 第2引数: LEDの個数(6)
  - bpp=4: RGBW形式(4要素)を使う設定

## 色の指定方法
- 色は (R, G, B, W) の4つの数値のタプルで指定する(各0〜255)
- 例: RED = (255, 0, 0, 0)、WHITE = (0, 0, 0, 255)、OFF = (0, 0, 0, 0)
- bpp=4(RGBW)で初期化しているため、色指定は必ず4要素のタプルにする(3要素だとエラーになる)

## LEDの制御方法
- `pixels[インデックス] = 色` で個別のLEDに色を設定する(インデックスは0〜5)
- 色を設定しただけでは反映されず、`pixels.write()` を呼んで初めて実機に反映される
- `time.sleep(秒)` で待機できる

## sample code
```python
import neopixel
from machine import Pin
import time
pixels = neopixel.NeoPixel(Pin(26), 6, bpp=4)
RED   = (255, 0, 0, 0)
BLUE  = (0, 0, 255, 0)
GREEN = (0, 255, 0, 0)
WHITE = (0, 0, 0, 255)
OFF   = (0, 0, 0, 0)
cnt = 0
while True:
    pixels[(0 + cnt)%6] = RED
    pixels[(1 + cnt)%6] = BLUE
    pixels[(2 + cnt)%6] = GREEN
    pixels[(3 + cnt)%6] = RED
    pixels[(4 + cnt)%6] = BLUE
    pixels[(5 + cnt)%6] = GREEN
    pixels.write()
    time.sleep(1)
    cnt += 1
```