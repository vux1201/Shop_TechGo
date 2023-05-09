<template>
  <h2 class="oder-h2">
    Danh sách quản lý đơn hàng <i class="fa-solid fa-cart-shopping"></i>
    <span class="sum-total"
      >Tổng tiền hàng : {{ formatPriceTotals(this.allTotal) }}</span
    >
    <!-- <span class="sum-total"
      >Tổng tiền hàng : <input v-model="this.allTotal"
    /></span
    > -->
    <span class="sum-total"
      >Đơn hàng đang vận chuyển : <input v-model="this.ship"
    /></span>
    <span class="sum-total"
      >Đơn hàng chờ xử lý : <input v-model="this.wait"
    /></span>
  </h2>
  <div class="oder-management">
    <div class="management-box">
      <div class="customer_orders">
        <div class="customer-table-wrap">
          <div class="customer-table">
            <div>
              <v-table>
                <thead>
                  <tr>
                    <th class="text-left">Mã đơn hàng</th>
                    <th class="text-left">Ngày đặt</th>
                    <th class="text-left">Thành tiền</th>
                    <th class="text-left">Trạng thái</th>
                    <th class="text-left">Vận chuyển</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    class="items-td"
                    v-for="item in admGetAllOders"
                    :key="item.menu"
                  >
                    <td class="item-code" @click="handleShowListOder(item.id)">
                      #{{ item.code }}
                      <span><i class="fa-solid fa-eye"></i></span>
                    </td>
                    <td>11/4/2023</td>
                    <td>{{ formatPriceTotals(item.total) }}</td>
                    <td class="item-status">
                      <v-switch
                        v-model="item.status"
                        @click="onAction(item)"
                      ></v-switch>
                      {{
                        item.status == false ? "Chờ xử lý" : "Đang giao hàng"
                      }}
                    </td>
                    <!-- <td>{{ item.status }}</td> -->
                    <td>
                      <v-switch
                        color="success"
                        v-model="this.onShipping"
                        @click="onShip"
                      ></v-switch>
                      {{
                        this.onShipping == false
                          ? "Chưa nhận hàng"
                          : "Đã nhận hàng"
                      }}
                    </td>
                  </tr>
                </tbody>
              </v-table>
              <div class="text-center">
                <v-pagination
                  v-model="page"
                  :length="3"
                  rounded="circle"
                  @update:modelValue="updatePage(page, size)"
                >
                </v-pagination>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="customer_orders" v-if="showListOder">
        <div class="customer-table-wrap">
          <div class="customer-table">
            <h4>Chi tiết đơn hàng {{ "#" + getOderId.code }}</h4>
            <div class="table-margin">
              <v-table>
                <thead>
                  <tr>
                    <th class="text-left items-img">Sản phẩm</th>
                    <th class="text-left">Mã sản phẩm</th>
                    <th class="text-left">Đơn giá</th>
                    <th class="text-left">Số lượng</th>
                    <th class="text-left">Thành tiền</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    class="items-td"
                    v-for="item in getOderId.order_items"
                    :key="item.name"
                  >
                    <td class="bl-flex">
                      <div class="bl-img">
                        <img
                          :src="item.product_variant.images?.[0]?.image_path"
                          alt=""
                        />
                      </div>
                      <span class="bl-name">{{
                        item.product_variant.name
                      }}</span>
                    </td>
                    <td>
                      <span>{{ item.product_variant.sku }}</span>
                    </td>
                    <td>
                      <span>{{
                        priceProductVariant(item.product_variant?.price)
                      }}</span>
                    </td>
                    <td>
                      <span>{{ item?.qty }}</span>
                    </td>
                    <td>
                      <span>
                        {{
                          totalPriceProductVariant(
                            item.product_variant?.price,
                            item?.qty
                          )
                        }}
                      </span>
                    </td>
                  </tr>
                </tbody>
              </v-table>
              <div class="block-body">
                <div class="block-p">
                  <p>Tổng tiền :</p>
                  <p style="margin-right: 16px">{{ totalPriceOder }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "pinia";
import { useOderStore } from "@/stores/oders";
export default {
  components: {},
  data() {
    return {
      showListOder: false,
      page: 1,
      size: 50,
      allTotal: 0,
      ship: 0,
      wait: 0,
      onShipping: false,
    };
  },

  async created() {
    try {
      await this.getAllOders(this.page, this.size);
      console.log("admGetAllOders", this.admGetAllOders);
      for (let i = 0; i < this.admGetAllOders.length; i++) {
        const sumTotal = this.admGetAllOders[i]?.total;
        this.allTotal += sumTotal;
        console.log(sumTotal, this.allTotal);
        if (this.admGetAllOders[i].status == 1) {
          this.ship += 1;
        } else {
          this.wait += 1;
        }
      }
      console.log(this.allTotal, "suM");
      console.log(this.ship);
      console.log(this.wait);
    } catch (error) {
      console.log(error);
    }
  },

  methods: {
    click(e) {
      console.log(e);
    },
    ...mapActions(useOderStore, ["getAllOders", "getOder", "putOder"]),
    async handleShowListOder(id) {
      try {
        await this.getOder(id);
        this.showListOder = true;
        console.log("getOderId1", this.getOderId);
      } catch (error) {}
    },
    formatPriceTotals(total) {
      return new Intl.NumberFormat("de-DE", {
        style: "currency",
        currency: "VND",
      }).format(total);
    },
    priceProductVariant(price) {
      return new Intl.NumberFormat("de-DE", {
        style: "currency",
        currency: "VND",
      }).format(price);
    },
    totalPriceProductVariant(price, qty) {
      let number = price * qty;
      return new Intl.NumberFormat("de-DE", {
        style: "currency",
        currency: "VND",
      }).format(number);
    },

    async onAction(item) {
      try {
        // 2 true, 3 false
        if (item.status == false) {
          item.status = 1;
          await this.putOder(item.id, item.status);
          console.log(item.status, "tus1");
        } else {
          item.status = 0;
          await this.putOder(item.id, item.status);
          console.log(item.status, "tus2");
        }
        // console.log(item.status);
        await this.getAllOders(this.page, this.size);
      } catch (error) {
        console.log(error);
      }
    },
    async onShip() {
      try {
        this.onShipping == true;
      } catch (error) {
        console.log(error);
      }
    },

    async updatePage(page, size) {
      try {
        this.skip = page;
        this.limit = size;
        await this.getAllOders(page, size);
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {
    ...mapState(useOderStore, ["admGetAllOders", "getOderId"]),

    totalPriceOder() {
      return new Intl.NumberFormat("de-DE", {
        style: "currency",
        currency: "VND",
      }).format(this.getOderId.total);
    },
  },
};
</script>

<style scoped>
.ustomer-table {
  position: relative;
}

.customer-table-wrap {
  background-color: #d9edf7;
  padding: 8px 10px;
  margin: 30px 0;
}

.customer-table-wrap {
  background-color: #d9edf7;
  padding: 8px 10px;
  margin: 30px 0;
}

.customer-table-wrap {
  background-color: #d9edf7;
  padding: 8px 10px;
  margin: 30px 0;
}

.customer-table-wrap {
  background-color: #d9edf7;
  padding: 8px 10px;
  margin: 30px 0;
}

.customer-table {
  background-color: white;
}

.customer-table h4 {
  padding: 4px 12px;
  border-bottom: 1px solid #d9edf7;
  color: black;
}

.text-left {
  width: 13.75%;
  text-align: center !important;
}

.items-img {
  width: 45%;
  text-align: left !important;
}

.items-td td {
  border-bottom: none !important;
  font-size: 0.82rem;
  margin-bottom: 12px;
  margin-top: 6px;
  text-align: center;
}

.bl-flex {
  display: flex;
}

.bl-img {
  width: 12%;
}

.bl-img img {
  width: 100%;
}

.bl-name {
  padding: 6px 12px;
}

.bl-name {
  padding: 6px 12px;
}

.table-margin {
  margin: 0 !important;
}

.block-body {
  border-top: 1px solid #d9edf7;
  margin-top: 24px;
}

.block-p {
  display: flex;
  justify-content: space-between;
  padding: 6px 20px;
  color: black;
}

.block-p p {
  font-weight: 500;
  font-size: 0.9rem;
}

.item-code {
  cursor: pointer;
}

.item-code:hover {
  color: #3498db;
}

:deep(.v-table__wrapper) {
  border-radius: 12px;
  overflow: hidden;
  margin-top: 30px;
}
:deep(.v-pagination__list) {
  color: black;
}

:deep(.v-table) {
  border-radius: 12px;
}

:deep(.v-table > .v-table__wrapper > table) {
  margin-top: 26px;
}

.table-margin :deep(.v-table > .v-table__wrapper > table) {
  margin-top: 0;
}

.item-status {
  display: flex;
  align-items: center;
  justify-content: center;
}

.oder-h2 {
  color: black;
  font-weight: 600 !important;
}

.sum-total {
  display: block;
  font-size: 1rem;
  margin-top: 20px;
}

.sum-total input {
  font-weight: bold;
  color: #2980b9;
}

:deep(.v-input__details) {
  display: none !important;
}

:deep(.v-input--density-default) {
  margin-left: 30px;
}

:deep(.v-switch .v-selection-control) {
  min-height: unset;
  display: unset;
}

:deep(.v-input) {
  flex: unset;
}

:deep(.v-switch .v-selection-control__wrapper) {
  margin-right: 12px;
}
</style>
