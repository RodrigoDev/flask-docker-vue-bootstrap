<template>
    <div class="container">
        <div class="row">
          <div class="col-sm-12">
            <form-wizard title="Seguro veicular" subtitle="Nunca foi tão fácil poupar!">
                <tab-content title="Veiculo">
                    <div class="form-group">
                        <label for="brand" class="form-label">Fabricante</label>
                        <select name="brand" id="" class="form-control">

                        </select>
                    </div>
                    <div class="form-group">
                        <label for="year" class="form-label">Ano de fabricação</label>
                        <select name="year" id="" class="form-control">

                        </select>
                    </div>
                </tab-content>
                <tab-content title="Condutores">
                    My second tab content
                </tab-content>
                <tab-content title="Finalizar">
                    Yuhuuu! This seems pretty damn simple
                </tab-content>
            
                </form-wizard>
            </div>
        </div>
    </div>
</template>

<script>
import Vue from 'vue';
import { FormWizard, TabContent } from 'vue-form-wizard';
import 'vue-form-wizard/dist/vue-form-wizard.min.css';

export default {
  name: 'Form',
  components: {
    FormWizard,
    TabContent,
  },
};

</script>
