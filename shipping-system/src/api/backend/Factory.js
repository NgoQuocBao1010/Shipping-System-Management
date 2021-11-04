import OrderRepo from "./OrderRepo";

const repositories = {
    order: OrderRepo,
};

export const RepositoryFactory = {
    get: (name) => repositories[name],
};
