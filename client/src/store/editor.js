import Vue from 'vue';
import { mergeLeft } from '@/utils/objMpl';

export default {
  namespaced: true,
  state: {
    objects: [],
    selectedObj: null,
    count: 0,
    someData: {
      first: 0,
      second: 0,
    },
  },
  mutations: {
    setSelectedObj: (state, param) => {
      state.selectedObj = param;
    },
    addObject: (state, param) => {
      Vue.set(state.someData, 'first', state.someData.first + 1);
      state.someData.first += 1;
      switch (param.code) {
        case 'text':
          state.objects.push([
            0,
            {
              type: param.code,
              value: '请双击输入文字',
              x: 70,
              y: 250,
              width: 180,
              font: 'SimHei',
              fontSize: 16,
              transparency: 0,
              borderWidth: 0,
              visibility: true,
            },
          ]);
          break;
        default:
          state.objects.push([
            0,
            {
              type: 'text',
              value: '请双击输入文字',
              x: 70,
              y: 250,
              width: 180,
              font: 'SimHei',
              fontSize: 16,
              transparency: 0,
              borderWidth: 0,
              visibility: true,
            },
          ]);
      }
    },
    updateProps(state, param) {
      Vue.set(state.objects[param.index], 1,
        mergeLeft(state.objects[param.index][1], param.propData));
    },
  },
};
