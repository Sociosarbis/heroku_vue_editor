<template>
  <div class="selector"
    :style="{
      top: y + 'px',
      left: x + 'px',
      width: width + 'px',
      height: height + 'px'
  }" v-drag>
    <div v-for="ptPos in ctrlpts" :key="ptPos" :data-pos="ptPos" :class="['ctrlpt', ptPos]" />
  </div>
</template>
<script>
import { mapState, mapMutations } from 'vuex';

export default {
  props: {
    ctrlpts: {
      type: Array,
      default() {
        return [
          'topLeft',
          'topMiddle',
          'topRight',
          'middleLeft',
          'middleRight',
          'bottomLeft',
          'bottomMiddle',
          'bottomRight',
        ];
      },
    },
  },
  computed: {
    ...mapState('editor', {
      index: state => state.selectedObj.index,
      x: state => state.selectedObj.customStyle.x,
      y: state => state.selectedObj.customStyle.y,
      width: state => state.selectedObj.customStyle.width,
      height: state => (state.selectedObj.customStyle.height === undefined ?
        state.selectedObj.$el.offsetHeight :
        state.selectedObj.customStyle.height),
    }),
  },
  methods: {
    ...mapMutations('editor', ['updateProps']),
  },
  directives: {
    drag: {
      inserted(el, binding, vnode) {
        el.addEventListener('mousedown', (e) => {
          e.preventDefault();
          const target = e.target.dataset.pos;
          const vm = vnode.context;
          let lastX = e.clientX;
          let lastY = e.clientY;
          function changePos(moveEvent) {
            moveEvent.preventDefault();
            let deltaX = moveEvent.clientX - lastX;
            let deltaY = moveEvent.clientY - lastY;
            const updateData = {
              index: vm.index,
              propData: null,
            };
            switch (target) {
              case 'topLeft':
                deltaX = Math.min(vm.width, deltaX);
                deltaY = Math.min(vm.height, deltaY);
                updateData.propData = {
                  x: vm.x + deltaX,
                  y: vm.y + deltaY,
                  width: vm.width - deltaX,
                  height: vm.height - deltaY,
                };
                break;
              case 'topMiddle':
                deltaY = Math.min(vm.height, deltaY);
                updateData.propData = {
                  y: vm.y + deltaY,
                  height: vm.height - deltaY,
                };
                break;
              case 'topRight':
                deltaX = Math.max(-vm.width, deltaX);
                deltaY = Math.min(vm.height, deltaY);
                updateData.propData = {
                  y: vm.y + deltaY,
                  width: vm.width + deltaX,
                  height: vm.height - deltaY,
                };
                break;
              case 'middleLeft':
                deltaX = Math.min(vm.width, deltaX);
                updateData.propData = {
                  x: vm.x + deltaX,
                  width: vm.width - deltaX,
                };
                break;
              case 'middleRight':
                deltaX = Math.max(-vm.width, deltaX);
                updateData.propData = {
                  width: vm.width + deltaX,
                };
                break;
              case 'bottomLeft':
                deltaX = Math.min(vm.width, deltaX);
                deltaY = Math.max(-vm.height, deltaY);
                updateData.propData = {
                  x: vm.x + deltaX,
                  width: vm.width - deltaX,
                  height: vm.height + deltaY,
                };
                break;
              case 'bottomMiddle':
                deltaY = Math.max(-vm.height, deltaY);
                updateData.propData = {
                  height: vm.height + deltaY,
                };
                break;
              case 'bottomRight':
                deltaX = Math.max(-vm.width, deltaX);
                deltaY = Math.max(-vm.height, deltaY);
                updateData.propData = {
                  width: vm.width + deltaX,
                  height: vm.height + deltaY,
                };
                break;
              default:
                updateData.propData = {
                  x: vm.x + deltaX,
                  y: vm.y + deltaY,
                };
            }
            vm.updateProps(updateData);
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
};
</script>
<style scoped>
.selector {
  position: absolute;
  border: 1px dashed black;
}
.ctrlpt {
  position: absolute;
  background: white;
  border: 1px solid black;
  width: 5px;
  height: 5px;
  transform: translate(-50%, -50%);
}
.topLeft {
  cursor: nwse-resize;
  top: 0px;
  left: 0px;
}
.topMiddle {
  cursor: ns-resize;
  top: 0px;
  left: 50%;
}
.topRight {
  cursor: nesw-resize;
  top: 0px;
  left: 100%;
}
.middleLeft {
  cursor: ew-resize;
  top: 50%;
  left: 0px;
}
.middleRight {
  cursor: ew-resize;
  top: 50%;
  left: 100%;
}
.bottomLeft {
  cursor: nesw-resize;
  top: 100%;
  left: 0px;
}
.bottomMiddle {
  cursor: ns-resize;
  top: 100%;
  left: 50%;
}
.bottomRight {
  cursor: nwse-resize;
  top: 100%;
  left: 100%;
}
</style>

