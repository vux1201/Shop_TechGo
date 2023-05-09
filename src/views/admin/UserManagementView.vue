<template>
  <h2 class="oder-h2">
    Danh sách quản lý người dùng <i class="fa-solid fa-users"></i>
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
                    <th class="text-left">ID</th>
                    <th class="text-left">Họ tên</th>
                    <th class="text-left">Email</th>
                    <th class="text-left">Số điện thoại</th>
                    <th class="text-left">Địa chỉ</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    class="items-td"
                    v-for="(user, index) in allUsers"
                    :key="index"
                  >
                    <td>{{ user.id }}</td>
                    <td
                      class="item-code"
                      v-if="user.firstname && user.lastname"
                      @click="handledetailUser(user.id)"
                    >
                      {{ user.firstname }} {{ user.lastname }}
                      <span v-if="user.firstname && user.lastname"
                        ><i class="fa-solid fa-eye"></i
                      ></span>
                    </td>
                    <td class="item-code" v-else>
                      <span>---</span>
                    </td>
                    <td>{{ user.email ? user.email : "---" }}</td>
                    <td>{{ user.phone_number ? user.phone_number : "---" }}</td>
                    <td class="item-status">
                      {{ user.address ? user.address : "---" }}
                    </td>
                  </tr>
                </tbody>
              </v-table>
              <div class="text-center">
                <v-pagination
                  v-model="page"
                  :length="totalPageUsers"
                  rounded="circle"
                  @update:modelValue="updatePage(page, size)"
                ></v-pagination>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="customer_orders" v-if="showUser">
        <div class="customer-table-wrap">
          <div class="customer-table">
            <h4>Thông tin người dùng</h4>
            <div class="table-margin">
              <v-table>
                <thead>
                  <tr>
                    <th class="text-left">Họ tên</th>
                    <th class="text-left">Email</th>
                    <th class="text-left">Số điện thoại</th>
                    <th class="text-left">Địa chỉ</th>
                    <th class="text-left">Quản trị viên</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="items-td">
                    <td style="display: flex">
                      <input
                        style="text-align: right"
                        v-model="this.detailUser.firstname"
                        disabled
                      />&nbsp;
                      <input
                        style="text-align: left"
                        v-model="this.detailUser.lastname"
                        disabled
                      />
                    </td>
                    <td>
                      <input v-model="this.detailUser.email" disabled />
                    </td>
                    <td>
                      <input v-model="this.detailUser.phone_number" disabled />
                    </td>
                    <td>
                      <input v-model="this.detailUser.address" disabled />
                    </td>
                    <td>
                      <input v-model="this.detailUser.is_admin" disabled />
                    </td>
                  </tr>
                </tbody>
              </v-table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "pinia";
import { useUsersStore } from "@/stores/users";
export default {
  components: {},
  data() {
    return {
      // dialog: false,
      page: 1,
      size: 10,
      showUser: false,
    };
  },
  methods: {
    ...mapActions(useUsersStore, ["getUsers", "getUser"]),
    async handledetailUser(id) {
      try {
        await this.getUser(id);
        this.showUser = true;
        console.log(id, "ied");
        console.log("detailUser", this.detailUser);
      } catch (error) {
        console.log(error);
      }
    },
    async updatePage(page, size) {
      try {
        let limit = this.size;
        let skip = this.page;
        await this.getUsers({ skip }, { limit });
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {
    ...mapState(useUsersStore, ["allUsers", "detailUser", "totalUsers"]),
    totalPageUsers() {
      return Math.ceil(this.totalUsers / this.size);
    },
  },
  async created() {
    try {
      let limit = this.size;
      let skip = this.page;
      await this.getUsers({ skip }, { limit });
      console.log("allUsers", this.allUsers);
    } catch (error) {
      console.log(error);
    }
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
  width: 22%;
  text-align: center !important;
}

/* .items-img {
  width: 45%;
  text-align: left !important;
} */

.items-td td {
  border-bottom: none !important;
  font-size: 0.82rem;
  margin-bottom: 12px;
  margin-top: 6px;
  text-align: center;
}
.items-td td input {
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

.fa-trash {
  margin-left: 18px;
}

.text-center {
  color: black;
}
</style>
