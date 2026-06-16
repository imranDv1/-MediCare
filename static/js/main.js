var csrftoken = $('meta[name="csrf-token"]').attr('content');
$.ajaxPrefilter(function(options, originalOptions, jqXHR) {
    if (options.type.toLowerCase() !== 'get') {
        jqXHR.setRequestHeader('X-CSRFToken', csrftoken);
    }
});

$(document).ready(function() {
    $('.sidebar-toggler, #sidebarToggler').on('click', function() {
        $('.sidebar').toggleClass('show');
        $('.sidebar').toggleClass('collapsed');
    });

    setTimeout(function() {
        $('.toast').toast('hide');
    }, 5000);

    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.map(function (el) { return new bootstrap.Tooltip(el) });

    $('.btn-delete').on('click', function(e) {
        if (!confirm('Are you sure you want to delete this item?')) {
            e.preventDefault();
        }
    });

    $('#select-all').on('change', function() {
        $('.select-item').prop('checked', this.checked);
    });

    if ($('input[type="date"]').length) {
        $('input[type="date"]').attr('placeholder', 'dd/mm/yyyy');
    }

    $('#sidebarOverlay').on('click', function() {
        $('.sidebar').removeClass('show');
    });

    $(document).on('click', 'a[href]:not([target="_blank"]):not([href^="#"]):not([href^="javascript"])', function(e) {
        var href = this.getAttribute('href');
        if (href && href !== '#' && !e.ctrlKey && !e.metaKey && !e.shiftKey) {
            $('#pageLoader').addClass('active');
        }
    });

});

function formatCurrency(amount) {
    return '$' + parseFloat(amount).toFixed(2);
}

function formatDate(dateStr) {
    if (!dateStr) return '-';
    var d = new Date(dateStr);
    return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
}
