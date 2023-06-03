$(function(){
    // Variables
    var drag_area = $('#drag-area');
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    var file;

    // Drag n Drop 
    drag_area.on('dragover', function(e){
        e.preventDefault();
        $('#header_text').html('Release to Upload!');
        $('#header_text').css({'font-weight':'bold', 'color':'#8f8f8f'});

        drag_area.addClass('active');
    })
    drag_area.on('dragleave', function(e){
        e.preventDefault();
        $('#header_text').html('Drag & Drop');
        $('#header_text').css({'font-weight':'normal', 'color':'#585858'})
        drag_area.removeClass('active');
    })
    drag_area.on('drop', function(e){
        e.preventDefault();
        $('#header_text').html('Drag & Drop');
        $('#header_text').css({'font-weight':'normal', 'color':'#585858'})
        drag_area.removeClass('active');

        var file_count = e.originalEvent.dataTransfer.files.length;
        if (file_count > 1){
            alert("Can't upload multiple files");
            return
        }

        file = e.originalEvent.dataTransfer.files[0];
        var file_type = file.type;
        console.log(file_type)
        if(file_type == 'text/csv' | file_type == 'application/vnd.ms-excel'){
            formData = new FormData();
            formData.append("file", file);

            // Ajax send file
            $.ajax({
                url: '/read_data',
                data: formData,
                processData: false,
                contentType: false,
                type: 'POST',
                beforeSend: function (xhr){
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                },
                success: function(data){
                    console.log(data);
                    $('#form').hide();
                    $('#result').show();
                    $('#filename').html(data.filename);
                    $.each(data.columns, function(index, value){
                        $('#dataX').find('select').append('<option value="'+index+'">'+value+'</option>')
                        $('#dataY').find('select').append('<option value="'+index+'">'+value+'</option>')
                        $('#dataZ').find('select').append('<option value="'+index+'">'+value+'</option>')
                        $('#query_col').find('select').append('<option value="'+index+'">'+value+'</option>')
                    })
                }
            });
        }else{
            alert("file not supported")
            return
        }
    })

    $('#generate-btn').on('click', function(){
        formData = new FormData();
        formData.append("filename", $('#filename').html());
        formData.append("charts", $('#charts option:selected').val());
        formData.append("x", $('#dataX').find('select option:selected').val());
        formData.append("y", $('#dataY').find('select option:selected').val());
        formData.append("z", $('#dataZ').find('select option:selected').val());
        formData.append("query_col", $('#query_col').find('select option:selected').val());
        formData.append("query_val", $('#query_val').find('select option:selected').val());
        $.ajax({
            url: '/generate_chart',
            data: formData,
            processData: false,
            contentType: false,
            type: 'POST',
            beforeSend: function (xhr){
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            },
            success: function(data){
                $('#visual-area').html(data.message)
            },
            error: function(data){
                console.log(data)
                alert(data.responseJSON.message)
            }
        });
    })

    $('#charts').on('change', function(){
        if ($(this).find('option:selected').val() == 'b_sp'){
            $('#dataY').show();
            $('#dataZ').hide();
            $('#query_col').hide();
            $('#query_val').hide();
            $('label[for="dataX"]').html('X :');
            $('label[for="dataY"]').html('Y :');
        }
        else if (jQuery.inArray($(this).find('option:selected').val(), ['b_lc', 'b_bp']) !== -1){
            $('#dataY').show();
            $('#dataZ').hide();
            $('#query_col').show();
            var value_select = $('#query_col').find('select');
            value_select.val('0').trigger('change');
            $('label[for="dataX"]').html('X :');
            $('label[for="dataY"]').html('Y :');
            ('label[for="query_col"]').html('Column :');
        }
        else if ($(this).find('option:selected').val() == 'b_bc'){
            $('#dataY').show();
            $('#dataZ').hide();
            $('#query_col').show();
            $('#query_val').hide();
            $('label[for="dataX"]').html('X :');
            $('label[for="dataY"]').html('Y :');
            $('label[for="query_col"]').html('Data :');
        }
        else if ($(this).find('option:selected').val() == 'b_pc'){
            $('#query_col').hide();
            $('#query_val').hide();
            $('#dataZ').hide();
            $('#dataY').show();
            $('label[for="dataX"]').html('Data :');
            $('label[for="dataY"]').html('Group :');
        }
        else if ($(this).find('option:selected').val() == 'b_h'){
            $('#dataZ').hide();
            $('#query_col').hide();
            $('#query_val').hide();
            $('#dataY').hide();
            $('label[for="dataX"]').html('X :');
        }
        else if ($(this).find('option:selected').val() == 'b_3lc'){
            $('#dataY').show();
            $('#dataZ').show();
            $('#query_col').show();
            var value_select = $('#query_col').find('select');
            value_select.val('0').trigger('change');
            $('label[for="dataX"]').html('X :');
            $('label[for="dataY"]').html('Y :');
            ('label[for="query_col"]').html('Column :');
        }
    })

    $('#query_col').find('select').on('change', function(){
        if (jQuery.inArray($('#charts').find('option:selected').val(), ['b_lc', 'b_bp', 'b_3lc']) !== -1){
            $.ajax({
                url: '/get_col_value?file='+$('#filename').html()+'&column_index='+$(this).find('option:selected').val(),
                type: 'GET',
                beforeSend: function (xhr){
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                },
                success: function(data){
                    $('#query_val').find('select').html(data.message);
                    $('#query_val').show();
                }
            });
        }
    })

    $('.btn-close').on('click', function(){
        window.location.reload();
    })
})

// Delete file from tmp when reloading page
window.onbeforeunload = function(){
    delete_file();
}

function delete_file(){
    formData = new FormData();
    formData.append("filename", $('#filename').html());
    $.ajax({
        url: '/delete_file',
        data: formData,
        processData: false,
        contentType: false,
        type: 'POST',
        beforeSend: function (xhr){
            xhr.setRequestHeader('X-CSRFToken', jQuery("[name=csrfmiddlewaretoken]").val());
        }
    });
}