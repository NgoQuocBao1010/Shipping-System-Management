import OrderRepo from "./OrderRepo";
import AccountRepo from "./AccountRepo";

const repositories = {
    order: OrderRepo,
    account: AccountRepo,
};

export const RepositoryFactory = {
    get: (name) => repositories[name],
};
