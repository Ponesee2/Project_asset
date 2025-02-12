// settings.js
$(document).ready(function() {
    // Show the settings modal when the settings button is clicked
    $('#settingsDropdown').on('click', function() {
        $('#settingsModal').modal('show');
        updateFormFromSettings(loadSettings());
    });

    // Apply saved settings on page load
    applySettings(loadSettings());

    // Add event listeners for setting changes
    $('.custom-control-input').on('change', function() {
        const settings = getSettingsFromForm();
        applySettings(settings);
        saveSettings(settings);
    });

    // Load settings from local storage
    function loadSettings() {
        const settings = localStorage.getItem('adminSettings');
        return settings ? JSON.parse(settings) : getDefaultSettings();
    }

    // Save settings to local storage
    function saveSettings(settings) {
        localStorage.setItem('adminSettings', JSON.stringify(settings));
    }

    // Get default settings
    function getDefaultSettings() {
        return {
            darkMode: false,
            headerFixed: false,
            dropdownLegacyOffset: false,
            noBorder: false,
            sidebarCollapsed: false,
            sidebarFixed: false,
            sidebarMini: false,
            sidebarMiniMD: false,
            sidebarMiniXS: false,
            navFlatStyle: false,
            navLegacyStyle: false,
            navCompact: false,
            navChildIndent: false,
            navChildHideOnCollapse: false,
            disableHoverFocusAutoExpand: false,
            footerFixed: false,
            smallTextBody: false,
            smallTextNavbar: false,
            smallTextBrand: false,
            smallTextSidebarNav: false
        };
    }

    // Get settings from the form inputs
    function getSettingsFromForm() {
        return {
            darkMode: $('#darkMode').is(':checked'),

            noBorder: $('#noBorder').is(':checked'),
            
            smallTextBody: $('#smallTextBody').is(':checked'),
            smallTextNavbar: $('#smallTextNavbar').is(':checked'),
            smallTextBrand: $('#smallTextBrand').is(':checked'),
            smallTextSidebarNav: $('#smallTextSidebarNav').is(':checked')
        };
    }

    // Update form inputs from settings
    function updateFormFromSettings(settings) {
        $('#darkMode').prop('checked', settings.darkMode);
      
        $('#noBorder').prop('checked', settings.noBorder);
       
        $('#smallTextBody').prop('checked', settings.smallTextBody);
        $('#smallTextNavbar').prop('checked', settings.smallTextNavbar);
        $('#smallTextBrand').prop('checked', settings.smallTextBrand);
        $('#smallTextSidebarNav').prop('checked', settings.smallTextSidebarNav);
    }

    // Apply settings to the page
    function applySettings(settings) {
        if (settings.darkMode) {
            document.documentElement.classList.add('dark-mode');
        } else {
            document.documentElement.classList.remove('dark-mode');
        }
       
        $('.navbar').toggleClass('no-border', settings.noBorder);
    
        $('.navbar').toggleClass('text-sm', settings.smallTextNavbar);
        $('.brand-link').toggleClass('text-sm', settings.smallTextBrand);
        $('.nav-sidebar').toggleClass('text-sm', settings.smallTextSidebarNav);
    }

    $(document).ready(function () {
        $('.selectpicker').selectpicker()
      })
});
