var Phenos = {
    init: function () {
        Phenos.autocomplete_disease();
    },

    autocomplete_disease : function() {
        $("#term").autocomplete({
            source:  function(request, response) {
                $.get('/phenos/diseases', { term : request.term }, function(data){
                    if (data != null) {
                        response($.map(data, function(disease){
                            return {
                                label: disease.fields["name"],
                                id: disease.pk
                            }
                        }));
                    }
                }, 'json');
            },
     
            select: function(event, ui){
                $('#hidden_field_disease_id').val(ui.item.value);
            }
        });
    }
}

Phenos.init();
