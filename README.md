# ![logo](https://solsort.com/_logo.png) Server backend for timelog app

Deployed at https://rasmuserik-timelog.appspot.com/

## API:

- `since`: timestamp, returns values equal to or newer than this. `since` must be integer
- `name`: the name of the storage to access
- `callback`: callback-name for jsonp
- `id`, `value`: something to store. write-only, name-id must be uniq. `id` must be integer

returns either `{error: "..."}` or a list of max 1000 elements newer than since. An element is: `{id: 123, value:'...', timestamp: 123}`.

