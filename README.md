# protobuf 3 example

https://protobuf.dev/

## compile

### golang
```sh
protoc -I=protobuf \
  --go_out=model/pb \
  --go_opt=Muser.proto=./ \
  user.proto
```

### python
```sh
protoc -I=protobuf \
  --python_out=model/pb \
  user.proto
```