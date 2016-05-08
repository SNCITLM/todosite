;(function () {
  'use strict'

  var nextHref = window.location

  $('#delete-modal').modal({
    backdrop: 'static',
    keyboard: false,
    show: false
  })

  $('#confirm-delete-todo').click(function () {
    window.location = nextHref
  })

  $('#cancel-delete-todo').click(function () {
    nextHref = window.location
  })

  $('.delete-button').click(function (e) {
    e.preventDefault()
    nextHref = e.currentTarget.href
    $('#delete-modal').modal('show')
  })

})()
