package utils

import (
	"crypto/md5"
	"encoding/hex"
)

func MD5(text string) string {
	hashSum := md5.Sum([]byte(text))
	return hex.EncodeToString(hashSum[:])
}
