function showAlert(message, messageTags) {
    swal.fire({
        title: messageTags,
        text: message,
        icon: messageTags,
        confirmButtonText: 'Ok'
    });
}
