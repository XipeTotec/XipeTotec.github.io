export interface ServiceContext {
  now: () => Date;
}

export function createServiceContext(): ServiceContext {
  return {
    now: () => new Date()
  };
}
