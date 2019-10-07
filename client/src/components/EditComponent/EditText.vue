<template>
  <div v-drag
    @click="setSelectedObj"
    :style="{
      top: customStyle.y + 'px',
      left: customStyle.x + 'px',
      width: customStyle.width + 'px',
      fontFamily: customStyle.font,
      fontSize: customStyle.fontSize + 'px',
      opacity: 1 - customStyle.transparency,
      borderWidth: 0 + 'px',
      display: customStyle.visibility === true? 'block': 'none'
  }">
    {{ customStyle.value }}
  </div>
</template>
<script>
export default {
  props: ['index', 'customStyle'],
  directives: {
    drag: {
      inserted(el, binding, vnode) {
        el.addEventListener('mousedown', (e) => {
          e.preventDefault();
          const vm = vnode.context;
          let lastX = e.clientX;
          let lastY = e.clientY;
          function changePos(moveEvent) {
            moveEvent.preventDefault();
            const x = (vm.customStyle.x + moveEvent.clientX) - lastX;
            const y = (vm.customStyle.y + moveEvent.clientY) - lastY;
            vm.$emit('changePos', {
              index: vm.index,
              propData: {
                x,
                y,
              },
            });
            lastX = moveEvent.clientX;
            lastY = moveEvent.clientY;
          }
          function removeListener(upEvent) {
            upEvent.preventDefault();
            document.removeEventListener('mousemove', changePos);
            document.removeEventListener('mouseup', removeListener);
          }
          document.addEventListener('mousemove', changePos, { passive: false });
          document.addEventListener('mouseup', removeListener, { passive: false });
        },
        { passive: false });
      },
    },
  },
  methods: {
    setSelectedObj() {
      this.$store.commit('editor/setSelectedObj', this);
    },
  },
};
</script>
<style scoped>
div {
  position: absolute;
}
</style>

