# Dockerfile for a custom Weaviate image setup
FROM cr.weaviate.io/semitechnologies/weaviate:1.28.0

# Set environment variables for the defaults
ENV QUERY_DEFAULTS_LIMIT=20 \
    AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED=true \
    PERSISTENCE_DATA_PATH="./data" \
    DEFAULT_VECTORIZER_MODULE="text2vec-transformers" \
    ENABLE_MODULES="text2vec-transformers" \
    CLUSTER_HOSTNAME="node1"

# Expose Weaviate ports
EXPOSE 8080 50051

CMD ["./weaviate"]
