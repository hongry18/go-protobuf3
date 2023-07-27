package main

import (
	"fmt"
	"io/ioutil"

	"github.com/hongry18/go-protobuf3/model/pb"
	"google.golang.org/protobuf/proto"
)

func main() {
	// person := pb.Person{
	// 	Id:    1234,
	// 	Name:  "hong",
	// 	Email: "hong@example.com",
	// 	Phones: []*pb.Person_PhoneNumber{
	// 		{Number: "1234", Type: pb.Person_PHONE_TYPE_HOME},
	// 	},
	// }

	// out, err := proto.Marshal(&person)
	// if err != nil {
	// 	panic(err)
	// }

	// fmt.Println(out)

	// var target pb.Person
	// if err := proto.Unmarshal(out, &target); err != nil {
	// 	fmt.Println(err)
	// }

	// fmt.Printf("-- %+v\n", target)

	in, err := ioutil.ReadFile("sample.txt")
	if err != nil {
		panic(err)
	}

	var t2 pb.Person
	if err := proto.Unmarshal(in, &t2); err != nil {
		fmt.Println(err)
	}
	fmt.Printf("-- %+v\n", t2)
}
