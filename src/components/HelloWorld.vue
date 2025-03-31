<script setup>
// 导入Vue的ref响应式API
import { ref } from 'vue'

// 定义组件的props，接收一个String类型的msg属性
defineProps({
  msg: String,
})

// 创建一个响应式的count变量，初始值为0
const count = ref(0)
</script>

<template>
  <!-- 显示从props接收的msg消息 -->
  <h1>{{ msg }}</h1>

  <div class="card">
    <!-- 点击按钮增加计数器的值 -->
    <button type="button" @click="count++">count is {{ count }}</button>
    <p>
      <!-- HMR（热模块替换）测试说明 -->
      Edit
      <code>components/HelloWorld.vue</code> to test HMR
    </p>
  </div>
  <!-- Vue官方文档链接 -->
  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
      >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Learn more about IDE Support for Vue in the
    <a
      href="https://vuejs.org/guide/scaling-up/tooling.html#ide-support"
      target="_blank"
      >Vue Docs Scaling up Guide</a
    >.
  </p>
  <!-- 提示用户点击logo了解更多信息 -->
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
</template>

<style scoped>
/* 设置文档提示文字的颜色为灰色 */
.read-the-docs {
  color: #888;
}
</style>
