import Vuex from 'vuex';
import Vue from 'vue';
import editor from './editor';

Vue.use(Vuex);

const store = new Vuex.Store({
  modules: {
    editor,
  },
});
export default store;

