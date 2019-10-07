<template>
  <div class="editor">
    <div class="main">
      <div class="arena">
        <component
          v-for="(object, index) in objects"
          :key="index"
          :is="'edit-' + object[1].type"
          :index="index"
          :customStyle="object[1]"
          @changePos="updateProps"
        >
        </component>
        <selector v-if="selectedObj !== null"/>
      </div>
    </div>
    <tool-list @addObject="addObject"/>
  </div>
</template>

<script>
import { mapMutations, mapState } from 'vuex';
import ToolList from './ToolList';
import EditText from './EditComponent/EditText';
import Selector from './Selector';

export default {
  name: 'HelloWorld',
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
    };
  },
  methods: {
    ...mapMutations('editor', ['addObject', 'updateProps']),
  },
  components: {
    'tool-list': ToolList,
    'edit-text': EditText,
    selector: Selector,
  },
  computed: {
    ...mapState('editor', ['objects', 'selectedObj']),
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.editor {
  display: flex;
  background: rgb(102, 102, 102);
}
.main {
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 1 1 100%;
}
.arena {
  width: 320px;
  height: 520px;
  background: #FFFFFF;
  position: relative;
}
</style>
