package database

import (
	"errors"
	"fmt"
	users "test/interface"
)

const LIMIT = 2

type Database[T users.Users] struct {
	objects []T
	size    int64
}

func (d Database[T]) GetSize() int64 {
	return d.size
}

func (d *Database[T]) Add(obj T) error {
	if d.size >= LIMIT {
		return errors.New(fmt.Sprintf("Size cannot exceed limit value %d", LIMIT))
	}
	d.objects = append(d.objects, obj)
	d.size += 1
	return nil
}

func (d *Database[T]) Delete(id int64) error {
	if d.size < id {
		return errors.New(fmt.Sprintf("ID cannot exceed limit value %d", d.size))
	} else if id < 0 {
		return errors.New(fmt.Sprintf("ID cannot be lower than minimum value 0"))
	}
	d.objects = append(d.objects[:id], d.objects[id+1:]...)
	d.size -= 1
	return nil
}

func (d Database[T]) String() string {
	retString := ""

	for _, obj := range d.objects {
		retString += obj.String()
		retString += " \n"
	}

	return retString
}
