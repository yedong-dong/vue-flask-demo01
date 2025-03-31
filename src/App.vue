<template>
  <div class="container">
    <BannerAndNav>
      
    </BannerAndNav>
  </div>
</template>

<script>
import BannerAndNav from './components/BannerAndNav.vue'
import { ref } from 'vue'
import { defineProps } from 'vue'
export default {
  components: {
    BannerAndNav
  },
  data() {
    return {
      message: '',
      isLoading: false
    }
  },
  methods: {
    async fetchMessage() {
      // 防止重复请求
      if (this.isLoading) return
      
      this.isLoading = true
      this.message = ''
      try {
        const response = await fetch('http://localhost:5000/api/test01')
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        const data = await response.json()
        this.message = data.message
      } catch (error) {
        console.error('Error:', error)
        this.message = '获取消息失败，请稍后重试'
      } finally {
        this.isLoading = false
      }
    }
  },
  mounted() {
    this.fetchMessage()
  }
}
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

.message-box {
  margin-top: 2rem;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
}

button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
  opacity: 0.7;
}

button.loading {
  position: relative;
  pointer-events: none;
}

button.loading::after {
  content: '';
  position: absolute;
  width: 16px;
  height: 16px;
  top: 50%;
  right: 10px;
  margin-top: -8px;
  border: 2px solid transparent;
  border-top-color: white;
  border-radius: 50%;
  animation: button-loading-spinner 1s linear infinite;
}

@keyframes button-loading-spinner {
  from {
    transform: rotate(0turn);
  }
  to {
    transform: rotate(1turn);
  }
}

button:hover {
  background-color: #45a049;
}
</style>
