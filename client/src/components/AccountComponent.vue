<script setup>
import { onMounted, ref, defineProps } from "vue";

const props = defineProps({
  account: {
    type: Object,
    required: true,
  },
});

// An account has : id, username, email, password, url

const account = ref(null);
const showPassword = ref(false);

onMounted(() => {
  account.value = props.account;
});
</script>

<template>
  <div>
    <q-card v-if="account">
      <q-card-section>
        <q-item-label header>{{ account.username }}</q-item-label>

        <q-item-label v-if="account.email" class="q-my-md">
          <span class="text-weight-bold">Email</span>
          <br />
          {{ account.email }}
        </q-item-label>

        <q-item-label class="q-my-md">
          <span class="text-weight-bold">Password</span>
          <br />
          <q-btn
            dense
            rounded
            icon="visibility"
            class="q-my-md q-mr-md"
            @click="showPassword = !showPassword"
          />
          <span v-if="showPassword">{{ account.password }}</span>
          <span v-else>********</span>
        </q-item-label>

        <q-item-label class="q-my-md">
          <span class="text-weight-bold">URL</span>
          <br />

          <!-- Use href, and wrap url if it's too long -->
          <a :href="account.url" target="_blank" class="text-decoration-none">
            <span v-if="account.url.length > 30">
              {{ account.url.slice(0, 30) }}...
            </span>
            <span v-else>
              {{ account.url }}
            </span>
          </a>
        </q-item-label>
      </q-card-section>
    </q-card>
  </div>
</template>
