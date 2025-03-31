<template>
  <div class="banner-container">
    <div class="top-banner">
      <div v-for="(name, index) in bannerNames" :key="index" class="banner-item"
        :class="{ active: activeBanner === index }" @click="selectBanner(index)">
        {{ name }}
      </div>
    </div>
    <div class="tab-content" :class="{ active: true }">
      <slot></slot>
    </div>

    <div class="nav-container">
      <div class="tab-content active">
        <!-- 导航菜单 -->
        <nav class="nav-menu">
          <ul>
            <template v-for="(item, index) in currentNav" :key="index">
              <li><a :href="item.href">{{ item.text }}</a></li>
            </template>
          </ul>
        </nav>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BannerAndNav',
  data() {
    return {
      bannerNames: ['Ahchat', 'HalaMe', 'Echo'],
      activeBanner: 0,
      ahchatNav: [
        { href: '#user-management', text: '用户管理' },
        { href: '#chat-history', text: '聊天记录' },
        { href: '#message-push', text: '消息推送' },
        { href: '#content-moderation', text: '内容审核' },
        { href: '#report-analysis', text: '数据报表' }
      ],
      halaNav: [
        { href: '#get-time-offset', text: '获取时间偏移' },
        { href: '#set-time-offset', text: '设置时间偏移' },
        { href: '#del-time-offset', text: '删除时间偏移' },
        { href: '#task-records', text: '任务领取记录' },
        { href: '#redis-keys', text: 'Redis Key 删除' },
        { href: '#set-vip', text: '设置VIP等级' },
        { href: '#set-influence-level', text: '设置网红等级' },
        { href: '#set-user-label', text: '模拟测试环境userlabel' },
        { href: '#get-token', text: '获取用户的token' }
      ],
      echoNav: [
        { href: '#live-stream', text: '直播管理' },
        { href: '#gift-system', text: '礼物系统' },
        { href: '#room-settings', text: '房间设置' },
        { href: '#audience-stats', text: '观众统计' },
        { href: '#stream-quality', text: '流质量监控' }
      ]
    }
  },
  computed: {
    currentNav() {
      switch(this.activeBanner) {
        case 0:
          return this.ahchatNav
        case 1:
          return this.halaNav
        case 2:
          return this.echoNav
        default:
          return []
      }
    }
  },
  methods: {
    selectBanner(index) {
      this.activeBanner = index
    }
  }
}
</script>

<style scoped>
.banner-container {
  width: 100%;
  box-sizing: border-box;
  padding-left: 250px;
  padding-top: 80px;
  position: relative;
}

.top-banner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 30px;
  background-color: #fff;
  max-width: 100%;
  position: fixed;
  top: 0;
  left: 250px;
  right: 0;
  z-index: 1000;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.nav-container {
  position: fixed;
  left: 0;
  top: 0;
  width: 250px;
  height: 100vh;
  background-color: #f5f5f5;
  box-shadow: 2px 0 4px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
}

.nav-menu {
  padding: 20px 0;
}

.nav-menu ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-menu li {
  padding: 0;
  margin: 0;
}

.nav-menu a {
  display: block;
  padding: 12px 20px;
  color: #333;
  text-decoration: none;
  font-size: 14px;
  transition: all 0.3s ease;
}

.nav-menu a:hover {
  background-color: rgba(76, 175, 80, 0.1);
  color: #4CAF50;
  padding-left: 25px;
}

.top-banner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 30px;
  background-color: #fff;
  max-width: 1200px;
  margin: 0 auto;
}

.banner-item {
  flex: 1;
  text-align: center;
  padding: 12px 24px;
  cursor: pointer;
  background-color: #fff;
  color: #333;
  margin: 0 12px;
  border-radius: 6px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: 2px solid #e0e0e0;
  font-weight: 500;
  position: relative;
  overflow: hidden;
}

.banner-item:hover {
  background-color: rgba(76, 175, 80, 0.1);
  transform: translateY(-2px);
  border-color: rgba(76, 175, 80, 0.5);
}

.banner-item.active {
  background-color: #4CAF50;
  color: white;
  border-color: #4CAF50;
  box-shadow: 0 4px 6px rgba(76, 175, 80, 0.2);
}

.banner-item::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  transform: translate(-50%, -50%);
  transition: width 0.3s ease-out, height 0.3s ease-out;
}

.banner-item:active::after {
  width: 100px;
  height: 100%;
}

.tab-content {
  padding: 20px;
}

/* 标签内容样式 */
.tab-content {
  display: none;
}

.tab-content.active {
  display: block;
}
</style>