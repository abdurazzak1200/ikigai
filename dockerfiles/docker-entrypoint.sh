COMMAND=$1

case "${1}" in
    "help")
        shift
        exec make help
        ;;
    *)
        shift
        exec make ${COMMAND}
        ;;
esac