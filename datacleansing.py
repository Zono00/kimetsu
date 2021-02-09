import cv2
import matplotlib.pyplot as pyplot
improt numpy as np
from keras.preprocessing.image import ImageDataGenerator
#for 文でリスト






#１、画像を持ってくる
imgs = cv2.imread("")
#２、訓練データ、テストデータに分ける
#連続しているシーンをスクショしているのでシャッフルしたい
rand_index = np.random.permutation(np.arange(len(imgs)))
imgs = imges[rand_index]
train_data = []
test_data = []

for img in imgs[0:350]:
    train_data.append(img)

for img in imgs[350:500]:
    test_data.append(img)

#写真は５００枚を想定し、それに白黒、反転でデータを水増し
def resize(dataset):
    my_img = cv2.resize(dataset, (100, 100))
    return my_img

def to_gray(dataset, x,y):
    for img in dataset[x, y]:
        my_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        dataset.append(my_img)
    return dataset
def to_flip(dataset, list, x, y):
    for img in dataset[x, y]:
        my_img = cv2.flip(img, 0)
        dataset.append(my_img)
    return dataset
resize(train_data)
resize(test_data)
to_gray(train_data)
to_gray(test_data)
to_flip(train_data)
to_flip(test_data)
#標準化
def to_normal(train_data, test_data):
    datagen = ImageDataGenerator(samplewise_center=True, samplewise_std_normalizetion=True)
    datagen.fit(train_data)
    g = datagen.flow(train_data, test_data, shuffle=False)
    X_batch, y_batch = g.next()
    return X_batch, y_batch
#これは訓練データにだけ用いるものなの？
#白色化
def no_correcation(train_data, test_data):
    dategen2 = ImageDataGenerator(featurewise_center=True, zca_whitening=True)
    datagen.fit(train_data)
    g = datagen.flow(train_data, test_data, shuffle = False)
    return

cv2.imwrite("train_set.jpg", train_data)
cv2.imwrite("test_set.jpg", test_data)




#raberuを貼る
#splitでラベルはり
for img in images:
    my_img = cv2.resize(img, (100,100))
    for img in images[0:150]:
        my_img = cv2.cvtColor(my_img, cv2.COLOR_RGB2GRAY)
        cv2.imwrite("togray.jpg", my_img)
#反転
    for img in images[150:300]:
        my_img = cv2.flip(my_img, 0)
        cv2.imwrite("flipimg.jpg", my_img)
    cv2.imwrite("dataset.jpg", my_img)

imges#ここをピクセルの最大をとってくる
#numpyで可能、全ての要素の最大
#その後CNNの標準化、白色化


#色変換も使うべき？
#さまざまな正規化やってみたい
#正規化はするべき
#この後正規化して、写真を全てシャッフル、訓練データ、テストデータに分けたい



#最後にtrain testを出力
