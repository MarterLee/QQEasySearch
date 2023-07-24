# item 实例化类

class CreativeDO:
    def __int__(self):
        self.itemId = 0
        self.shopId = 0
        self.itemName = "Not Define"
        self.itemCateName = "Not Define"
        self.itemCateId = 0
        self.itemSubCateName = "Not Define"
        self.itemSubCateId = 0
        self.matchScore = 0.0
        self.rankScore = 0.0
    # 构建商品侧特征
    def buildItemFeature(self):
        pass