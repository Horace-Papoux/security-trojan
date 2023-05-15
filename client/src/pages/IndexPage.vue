<script setup>
import { onMounted, ref } from "vue";
import { api } from "boot/axios";
import AccountComponentVue from "src/components/AccountComponent.vue";

const accounts = ref([]);

const fetchAccounts = async () => {
  const response = await api.get("/");
  accounts.value = response.data;

  // Remove account that have none of these : username, email, password and url
  accounts.value = accounts.value.filter((account) => {
    return account.username || account.email || account.password || account.url;
  });
};

onMounted(async () => {
  await fetchAccounts();
});
</script>

<template>
  <q-page>
    <h2 class="flex flex-center">Accounts list</h2>
    <div class="row q-col-gutter-md">
      <div class="col-3" v-for="account in accounts" :key="account.id">
        <AccountComponentVue :account="account" />
      </div>
    </div>
  </q-page>
</template>
