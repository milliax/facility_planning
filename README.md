# 設施規劃的期末模擬

## 架構規劃

commander
裡面負責派遣有幾台自走車
以及跑一個layout的圖
自走車的部分會需要單獨一個檔案
檔案跟檔案之間用zeroMQ連線

然後在layout的python中
顯示出來自走車以及地圖在這一個時間刻的狀態

## copilot generated

Commander: 負責派遣多台自走車。
Layout: 顯示自走車和地圖的狀態。
自走車: 每台自走車需要單獨一個檔案。
通信: 使用 ZeroMQ 來連接不同的檔案。
這個系統的工作流程大致如下：

Commander 負責派遣和管理多台自走車。
每台自走車有自己的獨立檔案，並通過 ZeroMQ 與 Commander 和 Layout 進行通信。
Layout 使用 Python 來顯示自走車和地圖在某一時間點的狀態。
這樣的系統可以用 Python 來實現。以下是實現這個系統的基本步驟：

使用 ZeroMQ 建立通信機制。
編寫 Commander 程式來派遣自走車。
編寫自走車的程式來接收指令並回報狀態。
編寫 Layout 程式來顯示自走車和地圖的狀態。