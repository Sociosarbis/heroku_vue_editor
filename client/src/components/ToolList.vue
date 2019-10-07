<template>
  <ul class="toolList">
    <li v-for="tool in tools" :key="tool.code" @click="$emit('addObject', {code: tool.code})">
      <div class="toolContainer">
        <div class="toolName">{{ tool.name }}</div>
        <div class="toolImg" :style="{ backgroundImage: 'url(' + tool.thumbnail +')'}"></div>
        <div class="tips">
          <div class="triangle-left"></div>
          {{ tool.tips }}
        </div>
        <div>{{ count }}</div>
      </div>
    </li>
  </ul>
</template>
<script>
import { mapState } from 'vuex';
import thumbnail from '../assets/thumbnail';

export default {
  data() {
    return {
      tools: [
        {
          name: '文字',
          code: 'text',
          thumbnail: thumbnail.text,
          tips: '点击添加一个文字组件',
        },
        {
          name: '图片',
          code: 'image',
          thumbnail: thumbnail.image,
          tips: '点击添加一张图片',
        },
        {
          name: '按钮',
          code: 'button',
          thumbnail: thumbnail.button,
          tips: '点击添加一个按钮',
        },
        {
          name: '音乐',
          code: 'music',
          thumbnail: thumbnail.music,
          tips: '点击添加背景音乐',
        },
      ],
    };
  },
  updated() {
    this.$nextTick(() => {
      console.log('irrelevant component updated');
    });
  },
  computed: mapState({
    count: (state) => {
      console.log(state.editor.someData.second);
      return state.editor.someData.first;
    },
  }),
};
</script>
<style scoped>
  .toolList {
    display: flex;
    flex-flow:column nowrap;
    width: 50px;
    background: #000000;
    padding: 0;
  }
  .toolContainer {
    display: flex;
    position: relative;
    justify-content: center;
    align-items: center;
    color: rgb(51, 51, 51);
    margin-top: 10px;
    padding: 0 5px;
  }
  .toolContainer:hover {
    color: #FFFFFF;
    background: #3D3D3D;
  }
  .toolContainer:hover .tips {
    display: initial;
    animation: scaleUp 0.2s;
  }
  .toolName {
    width: 20px;
  }
  .toolImg {
    width: 20px;
    height: 20px;
    background: no-repeat;
  }
  .tips {
    right: 70px;
    position: absolute;
    color: #FFFFFF;
    background: #000000;
    padding: 5px 10px;
    display: none;
    word-break: keep-all;
  }
  .tips .triangle-left {
    position: absolute;
    width: 0px;
    height: 0px;
    border-bottom: 5px solid transparent;
    border-top: 5px solid transparent;
    border-left: 10px solid black;
    right: 0px;
    transform-origin: 0% 50%;
    transform: translate3d(9px, 5px, 0);
  }
  @keyframes scaleUp {
    from {
      transform: scale(0)
    }
    to {
      transform: scale(1)
    }
  }
</style>
