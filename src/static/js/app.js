function updateOptions(options) {
  const update = {...options}
  if (localStorage.jwt) {
    update.headers = {
      ...update.headers,
      Authorization: `Bearer ${localStorage.jwt}`,
    }
  }
  return update
}

function fetcher(url, options) {
  return fetch(url, updateOptions(options));
}