var Phenos = {
    init: function () {
        var count = 0;
        Phenos.autocomplete_disease(count);
    },

    autocomplete_disease : function(count) {
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
                if(count < 1) {
                    $('#hidden_field_disease_id').val(ui.item.value);
                    count += 1;
                } else {
                    console.log("Yeah! You found me!");
                    error.error;
                }
            }
        });
    }
}

Phenos.init();
