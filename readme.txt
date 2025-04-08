1. 使用說明:
先設定input路徑於"input_path.txt"中，需填入絕對路徑，
再設定output路徑於"output_path.txt"中，需填入絕對路徑，
啟動bmp2jpg.exe，
程式即會根據input路徑中影像生成相應影像於output路徑，
其影像會是最高品質JPG影像(檔名保留)。

2.關於最高品質和檔案大小的一些知識:
BMP convert to JPG(在最高品質的前提下)
key point:
1. convert時要設定jpg的壓縮效率參數quality 為 100
2. convert時要將色彩子採樣設定為4:4:4
3. 以上參數設定後
壓縮比通常會在2:1 ~ 3:1之間 (根據Huffman編碼和 DCT變換的效率而定)
比如12MB的bmp image通常壓縮成jpg image後會變成6MB ~ 4MB之間
但可能會根據圖片狀況有所不同，影響的可能包含:
a. 影像中有較大面積的相似顏色，DCT變換壓縮效率會更好
b. 影像本身就含有較多資料冗餘被Huffman編碼減少，使得壓縮效率更好