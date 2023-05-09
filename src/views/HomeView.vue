<template>
  <div class="Home">
    <!-- ------------------------- banner--------------------------------------- -->
    <div class="home-banner">
      <div class="baner-up">
        <div class="home-baner-left">
          <div class="baner-img">
            <HomeBannerImageVue
              v-for="(url, i) in bannerUrlsLeft"
              :key="i"
              :url="url"
              @click="navigationListProducts()"
            >
            </HomeBannerImageVue>
          </div>
        </div>
        <!-- --------------------------------------------------------------->

        <div class="home-baner-center">
          <HomeSlideVue></HomeSlideVue>
        </div>
        <!-- --------------------------------------------------------------->

        <div class="home-baner-right">
          <div class="home-baner-right-img">
            <div>
              <HomeBannerImageVue
                v-for="(url, i) in bannerUrlsRight"
                :key="i"
                :url="url"
                @click="navigationListProducts()"
              ></HomeBannerImageVue>
            </div>
          </div>
        </div>
      </div>
      <!-- ---------------------------baner down------------------------------------ -->
      <div class="baner-bottom">
        <div class="baner-bottom-img">
          <HomeBannerImageVue
            v-for="(url, i) in bannerUrlsBottom"
            :key="i"
            :url="url"
            @click="navigationListProducts()"
          >
          </HomeBannerImageVue>
        </div>
      </div>

      <a class="phone" href="tel:1900.235.688" title="1900.235.688">
        <img
          src="data:image/png;base64,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"
        />
      </a>
      <!-- --------------------------HIGHLIGHTS CATEGORY------------------------------------->
      <div class="highlights-category">
        <h2>Danh mục nổi bật</h2>
        <div class="category-item">
          <HomeCategoryCardVue
            v-for="(category, i) in allCategory"
            :key="i"
            :url="category.image"
            :categotyTitles="category.name"
            @click="filterCategoty(category.id)"
          ></HomeCategoryCardVue>
        </div>
      </div>
      <!-- --------------------------------------------------------------->

      <div class="top-products">
        <div class="products-box">
          <div class="products-items">
            <h2>Top sản phẩm bán chạy</h2>
            <div class="slide-group">
              <v-sheet class="mx-auto" elevation="8" max-width="100%">
                <v-slide-group
                  v-model="model"
                  class="pa-4"
                  center-active
                  show-arrows
                >
                  <v-slide-group-item
                    v-for="(products, i) in topSellerProducts"
                    :key="i"
                    v-slot="{ isSelected, toggle }"
                  >
                    <v-card class="ma-4" width="218">
                      <ProductCardVue
                        :url="
                          products.product_variants[0]?.images[0].image_path
                        "
                        :name="products.name"
                        :brand="products.brand.name"
                        :price="products.product_variants[0]?.price"
                        :id="products.id"
                      >
                      </ProductCardVue>
                    </v-card>
                  </v-slide-group-item>
                </v-slide-group>
              </v-sheet>
            </div>
          </div>
        </div>
      </div>

      <!-- --------------------------------------------------------------- -->
      <div class="top-products-sale">
        <div class="products-box-sale">
          <div class="products-items">
            <div class="top-sale">
              <h2>Sản phẩm khuyến mại</h2>
              <div class="time-sale">
                <div class="time_products-sale">
                  <p>{{ timeDays }}</p>
                  <p class="time-sale-text">Days</p>
                </div>
                <div class="time_products-sale">
                  <p>{{ timesHours }}</p>
                  <p class="time-sale-text">Hours</p>
                </div>
                <div class="time_products-sale">
                  <p>{{ minutes }}</p>
                  <p class="time-sale-text">minutes</p>
                </div>
                <div class="time_products-sale">
                  <p>{{ seconds }}</p>
                  <p class="time-sale-text">seconds</p>
                </div>
              </div>
              <div class="container">
                <div class="header-right-address-Ripple">
                  <span style="--i: 1"></span>
                  <span style="--i: 2"></span>
                  <span style="--i: 3"></span>
                </div>
              </div>
            </div>
            <div class="slide-group slide-group-sale">
              <v-sheet class="mx-auto" elevation="8" max-width="100%">
                <v-slide-group
                  v-model="model"
                  class="pa-4"
                  center-active
                  show-arrows
                >
                  <v-slide-group-item
                    v-for="(products, i) in topSellerProducts"
                    :key="i"
                    v-slot="{ isSelected, toggle }"
                  >
                    <v-card class="ma-4" width="218">
                      <ProductCardVue
                        :url="
                          products.product_variants[0]?.images[0].image_path
                        "
                        :name="products.name"
                        :brand="products.brand.name"
                        :price="products.product_variants[0]?.price"
                        :id="products.id"
                      >
                      </ProductCardVue>
                    </v-card>
                  </v-slide-group-item>
                </v-slide-group>
              </v-sheet>
            </div>
            <div class="wrapper">
              <a href="#0" class="btn_add-cart">
                <span class="add-cards">Xem tất cả sản phẩm khuyến mãi</span>
                <span class="cart_span"
                  ><i class="fa-solid fa-angles-right"></i
                ></span>
                <div class="transition"></div>
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- --------------------------------------------------------------- -->
      <div class="new-product">
        <h2>Bộ sưu tập mới</h2>
        <div class="box-new-product">
          <div class="new-product-left">
            <img
              src="https://theme.hstatic.net/200000516791/1000880762/14/home_tabs_1_banner.jpg?v=2258"
              alt=""
            />
          </div>
          <div class="new-product-right">
            <div
              class="new-product-cart"
              v-for="(products, i) in newCollectionProducts"
              :key="i"
            >
              <ProductCardVue
                :url="products.product_variants[0]?.images[0].image_path"
                :name="products.name"
                :brand="products.brand.name"
                :price="products.product_variants[0]?.price"
                :id="products.id"
              >
              </ProductCardVue>
            </div>
          </div>
        </div>
      </div>

      <!-- --------------------------------------------------------------- -->

      <div class="hight-end-box">
        <h2>Sản phẩm cao cấp</h2>
        <div class="product-hight-end">
          <div
            class="hight-end-cart"
            v-for="(products, i) in highEndProducts"
            :key="i"
          >
            <ProductCardVue
              :url="products.product_variants[0]?.images[0].image_path"
              :name="products.name"
              :brand="products.brand.name"
              :price="products.product_variants[0]?.price"
              :id="products.id"
            >
            </ProductCardVue>
          </div>
        </div>
      </div>
    </div>

    <!-- ---------------------------------------------------------------- -->
  </div>
</template>

<script>
import { mapActions, mapState } from "pinia";
import { useProductsStore } from "@/stores/products";

import HomeBannerImageVue from "../components/HomeBannerImage.vue";
import HomeCategoryCardVue from "../components/HomeCategoryCard.vue";
import HomeSlideVue from "../components/HomeSlide.vue";
import ProductCardVue from "../components/ProductCard.vue";
// import { api } from '../api'

export default {
  components: {
    HomeSlideVue,
    HomeBannerImageVue,
    HomeCategoryCardVue,
    ProductCardVue,
  },

  data() {
    return {
      bannerUrlsLeft: [
        "https://telecomtalk.info/wp-content/uploads/2022/10/cropped-Apple-iPhone-14-Pro-and-Pro-Max-differences.jpg",
        "https://bizweb.dktcdn.net/100/176/601/collections/untitled-2-1-ef3e6f0b-cc6b-4d46-bc2f-b4f01071a61b.jpg?v=1663070166100",
      ],
      bannerUrlsRight: [
        "https://theme.hstatic.net/200000516791/1000880762/14/banner_top_1_img_large.jpg?v=2257",
        "https://theme.hstatic.net/200000516791/1000880762/14/banner_top_2_img_large.jpg?v=2257",
        "https://theme.hstatic.net/200000516791/1000880762/14/banner_top_3_img_large.jpg?v=2257",
      ],
      bannerUrlsBottom: [
        "https://theme.hstatic.net/200000516791/1000880762/14/categorybanner_1_img.jpg?v=2257",
        "https://theme.hstatic.net/200000516791/1000880762/14/categorybanner_2_img.jpg?v=2257",
        "https://theme.hstatic.net/200000516791/1000880762/14/categorybanner_3_img.jpg?v=2257",
        "https://theme.hstatic.net/200000516791/1000880762/14/categorybanner_4_img.jpg?v=2257",
      ],
      model: null,
      countDownToTime: new Date("May 30, 2023 00:00:00").getTime(),
      timeDays: null,
      timesHours: null,
      minutes: null,
      seconds: null,
      pageProduct: 1,
      sizeProduct: 10,
      pageCategory: 0,
      sizeCategory: 20,
    };
  },

  computed: {
    ...mapState(useProductsStore, [
      "allProducts",
      "allCategory",
      "params",
      "promotionProducts",
      "topSellerProducts",
      "newCollectionProducts",
      "highEndProducts",
    ]),
  },

  methods: {
    ...mapActions(useProductsStore, [
      "getProducts",
      "getPromotionProducts",
      "getTopSellerProducts",
      "getNewCollectionProducts",
      "getHighEndProducts",
      "getCategorys",
    ]),

    getAllProducts() {
      this.getPromotionProducts();
      this.getTopSellerProducts();
      this.getNewCollectionProducts();
      this.getHighEndProducts();
    },
    startTimer: function () {
      const timeNow = new Date().getTime();
      const timeDifference = this.countDownToTime - timeNow;
      const millisecondsInOneSecond = 1000;
      const millisecondsInOneMinute = millisecondsInOneSecond * 60;
      const millisecondsInOneHour = millisecondsInOneMinute * 60;
      const millisecondsInOneDay = millisecondsInOneHour * 24;
      const differenceInDays = timeDifference / millisecondsInOneDay - 1;
      const remainderDifferenceInHours =
        (timeDifference % millisecondsInOneDay) / millisecondsInOneHour;
      const remainderDifferenceInMinutes =
        (timeDifference % millisecondsInOneHour) / millisecondsInOneMinute;
      const remainderDifferenceInSeconds =
        (timeDifference % millisecondsInOneMinute) / millisecondsInOneSecond;
      const remainingDays = Math.floor(differenceInDays);
      const remainingHours = Math.floor(remainderDifferenceInHours);
      const remainingMinutes = Math.floor(remainderDifferenceInMinutes);
      const remainingSeconds = Math.floor(remainderDifferenceInSeconds);
      this.timeDays = remainingDays;
      this.timesHours = remainingHours;
      this.minutes = remainingMinutes;
      this.seconds = remainingSeconds;
    },

    navigationListProducts() {
      this.$router.push({ path: "/danh-sach-san-pham/:type" });
    },

    filterCategoty(id) {
      this.params.category_id = id;
      this.getProducts(this.params);
      this.$router.push({ path: "/danh-sach-san-pham/:type" });
    },
  },

  async created() {
    try {
      this.params.skip = this.pageProduct;
      this.params.limit = this.sizeProduct;
      await this.getProducts(this.params);

      this.params.skip = this.pageCategory;
      this.params.limit = this.sizeCategory;
      await this.getCategorys(this.params);

      //top sản phẩm khuyến mại
      this.params.skip = this.pageProduct;
      this.params.limit = this.sizeProduct;
      await this.getPromotionProducts(this.params);

      // sản phẩm bán chạy
      this.params.skip = this.pageProduct;
      this.params.limit = 14;
      // this.sizeProduct
      await this.getTopSellerProducts(this.params);

      // sản phẩm mới
      this.params.skip = this.pageProduct;
      this.params.limit = 10;
      // this.sizeProduct;
      await this.getNewCollectionProducts(this.params);

      // sản phẩm cao cấp
      this.params.skip = this.pageProduct;
      this.params.limit = this.sizeProduct;
      await this.getHighEndProducts(this.params);
    } catch (error) {
      console.log(error);
    }
  },
  mounted() {
    setInterval(() => {
      this.startTimer();
    }, 1000);
  },
};
</script>

<style scoped>
/* /// */
.home-header {
  position: relative;
}

.home-header-content {
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 2;
}

.home-banner {
  background-color: #ecf0f1;
}

.baner-up {
  display: flex;
}

.baner-img {
  margin-left: 50px;
  padding: 12px 6px;
}

.baner-img img {
  width: 100%;
  border-radius: 8px;
  transition: transform 0.2s;
  margin-bottom: 9px;
}

.baner-img img:hover {
  transform: scale(1.03);
}

.home-baner-left {
  width: 20%;
}

.home-baner-center {
  width: 55%;
}
.phone img {
  mix-blend-mode: multiply;
  width: 96px;
  position: fixed;
  top: 80vh;
  z-index: 99;
  left: 82rem;
}
.v-carousel__controls {
  display: none !important;
}

.v-carousel--hide-delimiter-background .v-carousel__controls {
  display: none;
}

.v-btn--icon.v-btn--density-default {
  color: white;
}

.home-baner-right {
  height: 425px;
  width: 25%;
  margin-right: 12px;
}

.home-baner-right-img {
  padding-left: 6px;
  padding-right: 18px;
  padding-top: 12px;
}

.home-baner-right-img div {
  height: 33%;
}

.home-baner-right-img img {
  width: 100%;
  height: 100%;
  border-radius: 8px;
  display: inline-block;
  margin-top: 0.5px;
  transition: transform 0.2s;
  margin-bottom: 7px;
}

.home-baner-right-img img:hover {
  transform: scale(1.03);
}

.baner-bottom {
  margin-left: 50px;
  padding-right: 24px;
}

.baner-bottom-img {
  width: 25%;
  display: flex;
}

.baner-bottom-img img {
  width: 100%;
  padding: 6px;
  border-radius: 20px;
  transition: transform 0.2s;
}

.baner-bottom-img img:hover {
  transform: scale(1.05);
}

.v-carousel--hide-delimiter-background .v-carousel__controls {
  display: none;
}

.highlights-category {
  background-color: white;
  margin-left: 55px;
  margin-right: 32px;
}

.highlights-category h2 {
  padding: 20px 16px;
  font-weight: 500;
  text-transform: capitalize;
}

.category-item {
  display: flex;
  flex-wrap: wrap;
}

.products-items {
  margin-left: 10px;
  padding: 12px;
}

.products-items h2 {
  margin-left: 41px;
  padding: 12px;
  text-transform: capitalize;
  font-weight: 600;
}

.products-box {
  margin-right: 16px;
}

/* .header-list {
  margin-top: 50px;
} */

.slide-group {
  padding-right: 4px;
  padding-left: 33px;
}

.slide-group-sale {
  padding-left: 0 !important;
}

.top-sale {
  display: flex;
  align-items: center;
  margin-bottom: 14px;
}

.top-sale h2 {
  text-transform: capitalize;
}

.time-sale {
  display: flex;
}

.time_products-sale {
  background-color: #fff200;
  color: #34495e;
  padding: 6px;
  text-align: center;
  margin: 0 8px;
  padding: 4px;
  width: 56px;
  border-radius: 20%;
}

.time_products-sale p {
  font-weight: 700;
}

.time-sale-text {
  font-size: 9px;
  font-weight: 500 !important;
}

:deep(.producCard-detail) {
  padding: 12px;
}

:deep(.v-carousel__controls) {
  display: none;
}

:deep(.v-window--show-arrows-on-hover:hover .v-window__left) {
  background-color: #2c3a47;
}

:deep(.v-window--show-arrows-on-hover:hover .v-window__right) {
  background-color: #2c3a47;
}

:deep(.mdi-chevron-left::before),
:deep(.mdi-chevron-right::before) {
  color: black;
  font-size: 2rem;
}

/* ::deep(.card) {
  margin-right: 0 !important;
  border-radius: none;
} */
.products-box-sale {
  background: #e55039;
  margin: 12px 32px 0 56px;
}

/* .top-products-sale .products-box-sale .products-items .slide-group .v-theme--light {
  background: #e55039;
} */

.products-box-sale .products-items h2 {
  color: #fffa65;
  font-weight: 600;
  margin: 0;
  padding: 12px 0;
  width: 46%;
}

:deep(
    .top-products-sale
      .products-box-sale
      .products-items
      .slide-group
      .v-theme--light
      .v-slide-group
      .v-slide-group__prev
      .mdi-chevron-left::before
  ),
:deep(
    .top-products-sale
      .products-box-sale
      .products-items
      .slide-group
      .v-theme--light
      .v-slide-group
      .v-slide-group__next
      .mdi-chevron-right::before
  ) {
  color: #f39c12;
}

:deep(.card) {
  margin-right: 0 !important;
  border-radius: 0;
  width: 100%;
  cursor: pointer;
}

:deep(.card__info) {
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
}

.container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container .header-right-address-Ripple {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: -2px;
  left: 20px;
  background: #fffa65;
  width: 5px;
  height: 5px;
  border-radius: 50%;
}

.container .header-right-address-Ripple span {
  position: absolute;
  border-radius: 50%;
  animation: animate 1s linear infinite;
  /* transform: rotateX(55deg); */
  animation-delay: calc(0.5s * var(--i));
  box-shadow: 0 1px 5px #fffa65;
}

.wrapper {
  text-align: center;
  width: 100%;
  position: relative;
}

.btn_add-cart {
  text-transform: uppercase;
  text-align: center;
  position: relative;
  text-decoration: none;
  display: inline-block;
}

.btn_add-cart:hover {
  color: black;
}

/* .btn_add-cart span {
  color: black;
} */

.btn_add-cart {
  /* width: 80%; */
  padding: 8px 24px;
  margin: 20px 0;
  font-size: 14px;
  color: #f1f2f6;
  text-align: center;
  text-transform: capitalize;
  border: 1px solid #fff;
  border-radius: 10px;
  position: relative;
  overflow: hidden !important;
  transition: all 0.3s ease-in-out;
  background: transparent !important;
  z-index: 1;
  border: 1px solid #ccc;
}

.btn_add-cart::before {
  content: "";
  width: 0%;
  height: 100%;
  display: block;
  background: #fff200;
  position: absolute;
  transform: skewX(-20deg);
  left: -10%;
  opacity: 1;
  top: 0;
  z-index: -12;
  transition: all 0.3s cubic-bezier(0.77, 0, 0.175, 1);
  box-shadow: 2px 0px 14px rgba(0, 0, 0, 0.6);
  color: #2c3a47;
}

.btn_add-cart::after {
  content: "";
  width: 0%;
  height: 100%;
  display: block;
  background: #f1f2f6;
  position: absolute;
  transform: skewX(-20deg);
  left: -10%;
  opacity: 0;
  top: 0;
  z-index: -15;
  box-shadow: 2px 0px 14px rgba(0, 0, 0, 0.6);
}

.btn_add-cart:hover::before {
  opacity: 1;
  width: 116%;
}

.cart_span {
  margin-right: 6px;
}

.add-cards {
  font-weight: 600;
  margin-right: 8px;
}

.new-product {
  margin: 12px 32px 0 56px;
}

.new-product h2 {
  margin-left: 10px;
  padding: 12px;
}

.box-new-product {
  display: flex;
}

.new-product-right {
  display: flex;
  width: 80%;
  flex-wrap: wrap;
}

.new-product-left {
  width: 20%;
}

.new-product-left img {
  width: 100%;
  height: 99%;
  object-fit: initial;
}

.new-product-cart {
  width: 20%;
  padding: 0 8px 12px 8px;
}

.product-hight-end {
  display: flex;
  width: 100%;
  flex-wrap: wrap;
}

.hight-end-cart {
  width: 20%;
  padding: 20px;
}

.hight-end-box {
  margin: 12px 32px 0 44px;
}

.hight-end-box h2 {
  margin-left: 10px;
  padding: 12px;
}

@keyframes animate {
  0% {
    width: 0;
    height: 0;
  }

  50% {
    opacity: 1;
  }

  100% {
    width: 30px;
    height: 30px;
  }
}
</style>
